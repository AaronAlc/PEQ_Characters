#/!/usr/bin/python
import re
import requests
from urllib.request import urlopen

from bs4 import BeautifulSoup
from lxml import html

from armor.models import Armor
from armor.models import Augmentation
from armor.models import EquipArmorSlot
from armor.models import EquipAugmentation1
from armor.models import EquipAugmentation2
from armor.models import WearableArmorSlot
from characters.models import Character

BASEURL = "http://www.projecteq.net/magelo/index.php?page=character&char="
AAURL = "http://www.projecteq.net/magelo/index.php?page=aas&char="

def getStat(stat, string):
    regex = "%s: \+?([0-9]+)" % (stat)
    match = re.search(regex, string)
    if match is not None:
        return (match.group(1))
    else :
        return 0

def getSlots(slot, string):
    regex = "%s:(.+)" % (slot)
    match = re.search(regex, string)
    slot_list = []
    if match is not None:
        slot_list = match.group(1).strip().split(' ')
        return (slot_list)
    return slot_list


def linkArmorToSlot(eas, character, armor, slot):
    if eas is None:
        eas = EquipArmorSlot(character=character, armor=armor, current_equip_slot=slot)
    else:
        if eas.armor.name != armor.name:
            eas.armor = armor 
        else:
            return
# overwrite the old one
    eas.save()


    
def findArmorSlotPossiblities(armor, slot_list):
    for slot in slot_list:
        slot = slot[:1] + slot[1:].lower()
        try:
            was = WearableArmorSlot.objects.get(armor=armor, wearable_armor_slot=slot)
        except :
            was = WearableArmorSlot(armor=armor, wearable_armor_slot=slot)
            was.save()

def updateCharacterAA(character):
    url = AAURL + character.name
    page = requests.get(url)
    tree = html.fromstring(page.content)

    title_xpath= "/html/head/title/text()"
    title = str(tree.xpath(title_xpath))

    if "Error" not in title:
        char_obj = Character.objects.get(name=character)
        aa_points_available_xpath = "//*[@id='charbrowser']/main/div[2]/div[3]/table/tbody/tr[1]/td[2]/text()"
        aa_points_spent_xpath = "//*[@id='charbrowser']/main/div[2]/div[3]/table/tbody/tr[2]/td[2]/text()"
        aa_avail_points =  int(str(tree.xpath(aa_points_available_xpath)[0]))
        aa_points_spent = int(str(tree.xpath(aa_points_spent_xpath)[0]))
        char_obj.aa_spent = aa_points_spent
        char_obj.aa_avail = aa_avail_points
        char_obj.save()

def updateCharacterAugmentations(character, eas, slot, augsEle):
    if eas != None:
        for i, innerAug in enumerate(augsEle):
        #get a new aug if not in db save it
            aug = findOrCreateAugmentation(innerAug)
            #use aug1 slot
            if aug is not None:
                if i == 0:
                    if eas.aug1 is None:
                        aug1 = findOrCreateAug1(aug)
                        aug1.save()
                        eas.aug1 = aug1
                        eas.save()
                    else:
                        print(eas.aug1.aug.name, aug.name)
                        if eas.aug1.aug.name != aug.name:
                            eas.aug1 = findOrCreateAug1(aug)
                            eas.save()
                elif i == 1:
                    if eas.aug2 is None:
                        aug2 = findOrCreateAug2(aug)
                        aug2.save()
                        eas.aug2 = aug2
                        eas.save()
                    else:
                        if eas.aug2.aug.name != aug.name:
                            eas.aug2 = findOrCreateAug2(aug)
                            eas.save()

def findOrCreateAug1(aug):
    try:
       newaug = EquipAugmentation1.objects.get(aug=aug)
    except EquipAugmentation1.DoesNotExist:
        newaug = EquipAugmentation1(aug=aug)
        newaug.save()
    return newaug

def findOrCreateAug2(aug):
    try:
        newaug = EquipAugmentation2.objects.get(aug=aug)
    except EquipAugmentation2.DoesNotExist:
        newaug = EquipAugmentation2(aug=aug)
        newaug.save()
    return newaug




def findOrCreateAugmentation(augEle):
    augName = augEle.find(class_="WindowNestedTanTitleBar").find("a").text
    try:
        aug = Augmentation.objects.get(name=augName)
    except Augmentation.DoesNotExist:
        augStatText = augEle.text
        strength = getStat("STR", augStatText)
        sta = getStat("STA", augStatText)
        agi = getStat("AGI", augStatText)
        dex  = getStat("DEX", augStatText)
        sta = getStat("STA", augStatText)
        cha = getStat("CHA", augStatText)
        wis = getStat("WIS", augStatText)
        intel = getStat("INT", augStatText)
        hps = getStat("HP", augStatText)
        mana = getStat("MANA", augStatText)
        end = getStat("Endurance", augStatText)
        ac = getStat("AC", augStatText)
        aug = Augmentation(name=augName, armor_class=ac,
                strength=strength, stamina=sta, agility=agi, dexterity=dex,
                wisdom=wis, intelligence=intel, charisma=cha, hp_points=hps,
                mana_points=mana,endurance_points=end)
        aug.save()
    return aug

def updateCharacterArmor(character):
    url = BASEURL + character.name
    page = requests.get(url)
    tree = html.fromstring(page.content)
    bs = BeautifulSoup(urlopen(url), "lxml")
     
#need to add a check right here to make sure the character is visible
    for armorSlotEnum in EquipArmorSlot.EQUIP_SLOTS:
        armorSlot= armorSlotEnum[0]
        xpath = "//*[@id='%s']/text()" % (armorSlot)

        ele = bs.find(id=armorSlot)
        if ele is not None:
            itemName = ele.find(class_="WindowTitleBar").find("a").text
            itemStatsEle = ele.find(class_="Stats")
            itemStatsText = itemStatsEle.text
            augsEle = itemStatsEle.find_all(class_="WindowNestedTan")
            for aug in augsEle:
                if aug is not None:
                    itemStatsText = itemStatsText.replace(aug.text, '').strip()
            try:
                armor = Armor.objects.get(name=itemName)
            except Armor.DoesNotExist:
                armor = None
                print("Creating new armor %s" %(itemName))
                strength = getStat("STR", itemStatsText)
                sta = getStat("STA", itemStatsText)
                agi = getStat("AGI", itemStatsText)
                dex  = getStat("DEX", itemStatsText)
                sta = getStat("STA", itemStatsText)
                cha = getStat("CHA", itemStatsText)
                wis = getStat("WIS", itemStatsText)
                intel = getStat("INT", itemStatsText)
                hps = getStat("HP", itemStatsText)
                mana = getStat("MANA", itemStatsText)
                end = getStat("Endurance", itemStatsText)
                ac = getStat("AC", itemStatsText)
                armor = Armor(name=itemName, armor_class=ac,
                        strength=strength, stamina=sta, agility=agi, dexterity=dex,
                        wisdom=wis, intelligence=intel, charisma=cha, hp_points=hps,
                        mana_points=mana,endurance_points=end)
                armor.save()
                findArmorSlotPossiblities(armor, armorSlot)
            try:
                #eas = EquipArmorSlot.objects.get(EQUIP_SLOTS=armorSlotEnum, char_id=character)
#get the current eas slot
                eas = EquipArmorSlot.objects.get(character=character, current_equip_slot=armorSlot)
            except:
                eas = None
            if armor is not None:
                linkArmorToSlot(eas, character, armor, armorSlot)
                updateCharacterAugmentations(character, eas, armorSlot, augsEle)

def getCharacterMagelo(character):
    url = BASEURL + character
    page = requests.get(url)
    tree = html.fromstring(page.content)
    title_xpath= "/html/head/title/text()"
    title = str(tree.xpath(title_xpath))
    

    try :
        character = Character.objects.get(name=character)
        if "Error" not in title:
            print("Updating %s" %(character))
            updateCharacterAA(character)
            updateCharacterArmor(character)
    except Character.DoesNotExist:
        print("This should never happen")

