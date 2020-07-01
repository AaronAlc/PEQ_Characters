import logging
import re
from typing import Tuple
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup
from lxml import html

from armor.models import Armor
from armor.models import Augmentation
from armor.models import EquipArmorSlot
from armor.models import WearableArmorSlot
from characters.models import Character

logger = logging.getLogger(__name__)
BASEURL = "http://www.projecteq.net/magelo/index.php?page=character&char="
AAURL = "http://www.projecteq.net/magelo/index.php?page=aas&char="


def get_stat(stat, string):
	regex = "%s: \+?([0-9]+)" % (stat)
	match = re.search(regex, string)
	if match is not None:
		return (match.group(1))
	else:
		return 0


def get_slots(slot, string):
	regex = "%s:(.+)" % (slot)
	match = re.search(regex, string)
	slot_list = []
	if match is not None:
		slot_list = match.group(1).strip().split(' ')
		return slot_list
	return slot_list


def link_armor_to_slot(eas, character, armor, slot):
	if eas is None:
		eas = EquipArmorSlot(character=character, armor=armor, current_equip_slot=slot)
	else:
		if eas.armor.name != armor.name:
			eas.armor = armor
		else:
			return
	# overwrite the old one
	eas.save()


def find_armor_slot_possiblities(armor, slot_list):
	for slot in slot_list:
		slot = slot[:1] + slot[1:].lower()
		try:
			was = WearableArmorSlot.objects.get(armor=armor, wearable_armor_slot=slot)
		except WearableArmorSlot.DoesNotExist:
			was = WearableArmorSlot(armor=armor, wearable_armor_slot=slot)
			was.save()


def update_character_aa(character):
	url = AAURL + character.name
	page = requests.get(url)
	tree = html.fromstring(page.content)

	title_xpath = "/html/head/title/text()"
	title = str(tree.xpath(title_xpath))

	if "Error" not in title:
		char_obj = Character.objects.get(name=character)
		aa_points_available_xpath = "//*[@id='charbrowser']/main/div[2]/div[3]/table/tbody/tr[1]/td[2]/text()"
		aa_points_spent_xpath = "//*[@id='charbrowser']/main/div[2]/div[3]/table/tbody/tr[2]/td[2]/text()"
		aa_avail_points = int(str(tree.xpath(aa_points_available_xpath)[0]))
		aa_points_spent = int(str(tree.xpath(aa_points_spent_xpath)[0]))
		char_obj.aa_spent = aa_points_spent
		char_obj.aa_avail = aa_avail_points
		char_obj.save()


def update_character_augmentations(character, eas, slot, augsEle):
	if eas is not None:
		for i, innerAug in enumerate(augsEle):
			# get a new aug if not in db save it
			aug = find_or_create_augmentation(innerAug)
			# use aug1 slot
			if aug is not None:
				if i == 0:
					if eas.aug1 is None:
						aug1 = find_or_create_aug1(aug)
						aug1.save()
						eas.aug1 = aug1
						eas.save()
					else:
						if eas.aug1.aug.name != aug.name:
							eas.aug1 = find_or_create_aug1(aug)
							eas.save()
				elif i == 1:
					if eas.aug2 is None:
						aug2 = find_or_create_aug2(aug)
						aug2.save()
						eas.aug2 = aug2
						eas.save()
					else:
						if eas.aug2.aug.name != aug.name:
							eas.aug2 = find_or_create_aug2(aug)
							eas.save()


def find_or_create_aug1(aug):
	try:
		newaug = EquipAugmentation1.objects.get(aug=aug)
	except EquipAugmentation1.DoesNotExist:
		newaug = EquipAugmentation1(aug=aug)
		newaug.save()
	return newaug


def find_or_create_aug2(aug):
	try:
		newaug = EquipAugmentation2.objects.get(aug=aug)
	except EquipAugmentation2.DoesNotExist:
		newaug = EquipAugmentation2(aug=aug)
		newaug.save()
	return newaug


def find_or_create_augmentation(augEle):
	aug_name = augEle.find(class_="WindowNestedTanTitleBar").find("a").text
	try:
		aug = Augmentation.objects.get(name=aug_name)
	except Augmentation.DoesNotExist:
		aug_stat_text = augEle.text
		strength = get_stat("STR", aug_stat_text)
		sta = get_stat("STA", aug_stat_text)
		agi = get_stat("AGI", aug_stat_text)
		dex = get_stat("DEX", aug_stat_text)
		sta = get_stat("STA", aug_stat_text)
		cha = get_stat("CHA", aug_stat_text)
		wis = get_stat("WIS", aug_stat_text)
		intel = get_stat("INT", aug_stat_text)
		hps = get_stat("HP", aug_stat_text)
		mana = get_stat("MANA", aug_stat_text)
		end = get_stat("Endurance", aug_stat_text)
		ac = get_stat("AC", aug_stat_text)
		aug = Augmentation(name=aug_name, armor_class=ac,
		                   strength=strength, stamina=sta, agility=agi, dexterity=dex,
		                   wisdom=wis, intelligence=intel, charisma=cha, hp_points=hps,
		                   mana_points=mana, endurance_points=end)
		aug.save()
	return aug


def update_character_armor(character):
	url = BASEURL + character.name
	page = requests.get(url)
	tree = html.fromstring(page.content)
	bs = BeautifulSoup(urlopen(url), "lxml")

	# need to add a check right here to make sure the character is visible
	for armorSlotEnum in EquipArmorSlot.EQUIP_SLOTS:
		armor_slot = armorSlotEnum[0]
		xpath = "//*[@id='%s']/text()" % (armor_slot)

		ele = bs.find(id=armor_slot)
		if ele is not None:
			item_name = ele.find(class_="WindowTitleBar").find("a").text
			item_stats_ele = ele.find(class_="Stats")
			item_stats_text = item_stats_ele.text
			augs_ele = item_stats_ele.find_all(class_="WindowNestedTan")
			for aug in augs_ele:
				if aug is not None:
					item_stats_text = item_stats_text.replace(aug.text, '').strip()
			try:
				armor = Armor.objects.get(name=item_name)
			except Armor.DoesNotExist:
				armor = None
				strength = get_stat("STR", item_stats_text)
				sta = get_stat("STA", item_stats_text)
				agi = get_stat("AGI", item_stats_text)
				dex = get_stat("DEX", item_stats_text)
				sta = get_stat("STA", item_stats_text)
				cha = get_stat("CHA", item_stats_text)
				wis = get_stat("WIS", item_stats_text)
				intel = get_stat("INT", item_stats_text)
				hps = get_stat("HP", item_stats_text)
				mana = get_stat("MANA", item_stats_text)
				end = get_stat("Endurance", item_stats_text)
				ac = get_stat("AC", item_stats_text)
				armor = Armor(name=item_name, armor_class=ac,
				              strength=strength, stamina=sta, agility=agi, dexterity=dex,
				              wisdom=wis, intelligence=intel, charisma=cha, hp_points=hps,
				              mana_points=mana, endurance_points=end)
				armor.save()
				find_armor_slot_possiblities(armor, armor_slot)
			try:
				eas = EquipArmorSlot.objects.get(character=character, current_equip_slot=armor_slot)
			except EquipArmorSlot.DoesNotExist:
				eas = None
			if armor is not None:
				link_armor_to_slot(eas, character, armor, armor_slot)
				update_character_augmentations(character, eas, armor_slot, augs_ele)


def update_character(character):
	url = BASEURL + character
	page = requests.get(url)
	tree = html.fromstring(page.content)
	title_xpath = "/html/head/title/text()"
	title = str(tree.xpath(title_xpath))

	try:
		character = Character.objects.get(name=character)
		if "Error" not in title:
			logger.info("Updating %s" % character)
			update_character_aa(character)
			update_character_armor(character)
	except Character.DoesNotExist:
		logger.error("This should never happen")
