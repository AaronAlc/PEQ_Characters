from django.db import models

from django.apps import apps

# Create your models here.
class ItemAttributes(models.Model):
    name=models.CharField(max_length=100)
    armor_class=models.IntegerField(default=0)
    strength=models.IntegerField(default=0)
    stamina=models.IntegerField(default=0)
    agility=models.IntegerField(default=0)
    dexterity=models.IntegerField(default=0)
    wisdom=models.IntegerField(default=0)
    intelligence=models.IntegerField(default=0)
    charisma=models.IntegerField(default=0)
    hp_points=models.IntegerField(default=0)
    mana_points=models.IntegerField(default=0)
    endurance_points=models.IntegerField(default=0)
    spell_shielding=models.IntegerField(default=0)
    shieldling=models.IntegerField(default=0)
    focus_effect = models.CharField(max_length=100, default=None, null=True, blank=True)

    class Meta:
        abstract=True

class Augmentation(ItemAttributes):
    augmentation_id=models.AutoField(primary_key=True)

    ANGUISH_AUG_NAMES = [
        "Rune of Futile Resolutions",
        "Stone of Horrid Transformation",
        "Rune of Grim Portents",
        "Rune of Living Lightning",
        "Gem of Unnatural Regrowth",
        "Stone of Planar Protection",
        "Rune of Astral Celerity",
        "Abhorrent Brimstone of Charring",
        "Orb of Forbidden Laughter",
        "Petrified Girplan Heart",
        "Kyv Eye of Marksmanship",
    ]

    class Meta:
        db_table = "Augmentation"

    def __str__(self):
        return self.name

class EquipAugmentation1(models.Model):
    equip_aug_slot1 = models.AutoField(primary_key=True)
    aug = models.ForeignKey(Augmentation, on_delete=models.CASCADE)

    def __str__(self):
        return self.aug.name

    class Meta:
        db_table = "Equip_Augmentation_Slot1"

class EquipAugmentation2(models.Model):
    equip_aug_slot2 = models.AutoField(primary_key=True)
    aug = models.ForeignKey(Augmentation, on_delete=models.CASCADE)

    class Meta:
        db_table = "Equip_Augmentation_Slot2"

    def __str__(self):
        return self.aug.name

class Armor(ItemAttributes):
    armor_id=models.AutoField(primary_key=True)

    class Meta:
        db_table = "Armor"
        verbose_name_plural = 'Armor'

    def __str__(self):
        return self.name

class EquipArmorSlot(models.Model):
    equip_slot_id = models.AutoField(primary_key=True)
    EQUIP_SLOTS = (
        ('slot0', 'Charm'),
        ('slot1', 'LeftEar'),
        ('slot2', 'Head'),
        ('slot3', 'Face'),
        ('slot4', 'RightEar'),
        ('slot5', 'Neck'),
        ('slot6', 'Shoulder'),
        ('slot7', 'Arms'),
        ('slot8', 'Back'),
        ('slot9', 'LeftWrist'),
        ('slot10', 'RightWrist'),
        ('slot11', 'Range'),
        ('slot12', 'Hands'),
        ('slot13', 'Primary'),
        ('slot14', 'Secondary'),
        ('slot15', 'LeftFinger'),
        ('slot16', 'RightFinger'),
        ('slot17', 'Chest'),
        ('slot18', 'Legs'),
        ('slot19', 'Feet'),
        ('slot20', 'Waist'),
        ('slot21', 'Ammo'),
        ('slot22', 'PowerSource'),
    )
    character = models.ForeignKey('characters.Character', on_delete=models.CASCADE)
    armor = models.ForeignKey('armor.Armor', on_delete=models.CASCADE)
    current_equip_slot = models.CharField(max_length=6, choices=EQUIP_SLOTS, default=None, null=True)
    aug1 = models.ForeignKey(EquipAugmentation1, on_delete=models.CASCADE, default=None, null=True)
    aug2 = models.ForeignKey(EquipAugmentation2, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        db_table = 'Equip_Armor_Slot'
    def slot_verbose(self):
        return dict(EquipArmorSlot.EQUIP_SLOTS)[self.current_equip_slot]

class WearableArmorSlot(models.Model):
    wear_slot_id = models.AutoField(primary_key=True)
    WEARABLE_SLOTS = (
        ('Charm', 'Charm'),
        ('Ears', 'Ears'),
        ('Head', 'Head'),
        ('Face', 'Face'),
        ('Neck', 'Neck'),
        ('Shoulders', 'Shoulders'),
        ('Arms', 'Arms'),
        ('Back', 'Back'),
        ('Wrists', 'Wrists'),
        ('Range', 'Range'),
        ('Hands', 'Hands'),
        ('Primary', 'Primary'),
        ('Secondary', 'Secondary'),
        ('Fingers', 'Fingers'),
        ('Chest', 'Chest'),
        ('Legs', 'Legs'),
        ('Feet', 'Feet'),
        ('Waist', 'Waist'),
        ('Ammo', 'Ammo'),
    )
    armor = models.ForeignKey('armor.Armor', null=True, blank=True, on_delete=models.CASCADE, default=None)
    wearable_armor_slot = models.CharField(max_length=15, choices=WEARABLE_SLOTS, default=None, blank=True)

    class Meta:
        db_table = 'Wearable_Armor_Slot'

