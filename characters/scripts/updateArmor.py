#/!/usr/bin/python
from bs4 import BeautifulSoup
from urllib.request import urlopen
from characters.models import Character
from armor.models import Armor, EquipArmorSlot, WearableArmorSlot
import re

BASEURL = "http://www.peqtgc.com/magelo/index.php?page=character&char="

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
    try:
        eas = EquipArmorSlot.objects.get(character=character, armor=armor, current_equip_slot=slot)
    except:
        eas = EquipArmorSlot(character=character, armor=armor, current_equip_slot=slot)
        eas.save()

def findArmorSlotPossiblities(armor, slot_list):
    for slot in slot_list:
        slot = slot[:1] + slot[1:].lower()
        try:
            was = WearableArmorSlot.objects.get(armor=armor, wearable_armor_slot=slot)
        except :
            was = WearableArmorSlot(armor=armor, wearable_armor_slot=slot)
            was.save()

def getCharacterMagelo(character):
    url = BASEURL + character
    bs = BeautifulSoup(urlopen(url), 'lxml')
    itemDivs = bs.findAll('div', id=True)
    for div in itemDivs:
        div_id = div['id']
        if div_id.startswith('slot'):
            try:
                slot_num = int(div_id[4:])
                item_name = div.find('div', attrs={'class', 'ItemTitleMid', 'style', 'text-align:left'}).text
                item_stats = div.find('div', attrs={'class', 'ItemInner'}).text
                aug_text = div.find('table', attrs={'class', 'AugTable'})
                armor_slots = getSlots("Slot", item_stats)
                if aug_text is not None:
                    aug_text = aug_text.text.strip()
                    item_stats = item_stats.replace(aug_text, '').strip()
                if(slot_num < 23):
                    try:
                        armor = Armor.objects.get(name=item_name)
                    except Armor.DoesNotExist:
                        armor = None
                    try:
                        character = Character.objects.get(name=character)
                    except Character.DoesNotExist:
                        print("This should never happen")
                        print("***CHARACTER DOES NOT EXIST")
                    if armor is None:
                        strength = getStat("STR", item_stats)
                        sta = getStat("STA", item_stats)
                        agi = getStat("AGI", item_stats)
                        dex  = getStat("DEX", item_stats)
                        sta = getStat("STA", item_stats)
                        cha = getStat("CHA", item_stats)
                        wis = getStat("WIS", item_stats)
                        intel = getStat("INT", item_stats)
                        hps = getStat("HP", item_stats)
                        mana = getStat("MANA", item_stats)
                        end = getStat("Endurance", item_stats)
                        ac = getStat("AC", item_stats)
                        armor = Armor(name=item_name, armor_class=ac,
                                strength=strength, stamina=sta, agility=agi, dexterity=dex,
                                wisdom=wis, intelligence=intel, charisma=cha, hp_points=hps,
                                mana_points=mana,endurance_points=end)
                        armor.save()
                    try:
                        eas = EquipArmorSlot.objects.get(EQUIP_SLOTS=equip_slot, char_id=character)
                    except :
                        eas = None
                    findArmorSlotPossiblities(armor, armor_slots)
                    linkArmorToSlot(eas, character, armor, div_id)
            except ValueError or Exception:
                print ("Not a valid number Will ignore Tag: %s" %(div_id))

##def getCharacterMagelo(character):
##    url = BASEURL + character
##    bs = BeautifulSoup(urlopen(url), 'lxml')
##    itemDivs = bs.findAll('div', id=True)
##    for div in itemDivs:
##        div_id = div['id']
##        if div_id.startswith('slot'):
##            try:
##                slot_num = int(div_id[4:])
##                item_name = div.find('div', attrs={'class', 'ItemTitleMid', 'style', 'text-align:left'}).text
##                item_stats = div.find('div', attrs={'class', 'ItemInner'}).text
##                aug_text = div.find('table', attrs={'class', 'AugTable'})
##                if aug_text is not None:
##                    aug_tekkkkkkkkkkkkkkxt = aug_text.text.strip()
##                    item_stats = item_stats.replace(aug_text, '').strip()
##                if(slot_num < 23):
##                    strength = getStat("STR", item_stats)
##                    sta = getStat("STA", item_stats)
##                    agi = getStat("AGI", item_stats)
##                    dex  = getStat("DEX", item_stats)
##                    sta = getStat("STA", item_stats)
##                    cha = getStat("CHA", item_stats)
##                    hps = getStat("HP", item_stats)
##                    mana = getStat("MANA", item_stats)
##                    end = getStat("Endurance", item_stats)
##                    slots = getSlots("Slot", item_stats)
##                    print(item_name, strength, sta, item_stats)
##            except ValueError or Exception:
##                print ("Not a valid number Will ignore Tag: %s" %(div_id))
##
##getCharacterMagelo("Loewit")
#need to link character and armor
#need to link character and armor
#need to link character and armor
#need to link character and armor
#need to link character and armor
#need to link character and armor
#need to link character and armor
#need to link character and armor
#need to link character and armor
