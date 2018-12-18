from django.db import models

from django.apps import apps

# Create your models here.
class Armor(models.Model):
    armor_id=models.AutoField(primary_key=True)
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
    current_equip_slot = models.CharField(max_length=6, choices=EQUIP_SLOTS, default=None, blank=True, null=True)

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
        ('Powersource', 'Powersource'),
    )
    armor = models.ForeignKey('armor.Armor', on_delete=models.CASCADE)
    wearable_armor_slot = models.CharField(max_length=15, choices=WEARABLE_SLOTS, default=None, blank=True)
