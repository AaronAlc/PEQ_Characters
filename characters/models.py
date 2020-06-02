from django.db import models
from django.contrib import admin
from django.apps import apps

# Create your models here.
class Character(models.Model):
    CHAR_CLASSES = (
        ('WAR', 'Warrior'),
        ('CLR', 'Cleric'),
        ('PAL', 'Paladin'),
        ('RNG', 'Ranger'),
        ('SHD', 'Shadow Knight'),
        ('DRU', 'Druid'),
        ('BRD', 'Bard'),
        ('ROG', 'Rogue'),
        ('SHM', 'Shaman'),
        ('NEC', 'Necromancer'),
        ('WIZ', 'Wizard'),
        ('MAG', 'Magician'),
        ('ENC', 'Enchanter'),
        ('BST', 'Beastlord'),
        ('BER', 'Berserker'),
        ('MNK', 'Monk'),
    )

    CHAR_SETS = {
        ('Plate', 'Plate'),
        ('Chain', 'Chain'),
        ('Leather', 'Leather'),
        ('Silk', 'Silk'),
        ('Priests', 'Priests'),
        ('Melee', 'Melee'),
        ('Casters', 'Casters'),
    }

    CHAR_SETS_LOOK_UP = {
        'Plate': ['WAR', 'CLR', 'SHD', 'PAL', 'BRD'],
        'Silk': ['NEC', 'WIZ', 'MAG','ENC'],
        'Chain': ['RNG', 'ROG', 'SHM', 'BER'],
        'Leather': ['DRU', 'BST', 'MNK'],
        'Priests': ['CLR', 'SHM', 'DRU'],
        'Melee': ['WAR', 'PAL', 'RNG', 'SHD', 'BRD', 'ROG', 'BST', 'BER', 'MNK'],
        'Casters': ['CLR','DRU', 'SHM', 'NEC', 'WIZ', 'MAG', 'ENC',],
    }

    char_id = models.AutoField(primary_key=True)
    char_class = models.CharField(max_length=3, choices=CHAR_CLASSES)
    name = models.CharField(max_length=30)
    level = models.IntegerField(default=1)
    aa_spent = models.IntegerField(default=0)
    aa_avail = models.IntegerField(default=0)
    def getTotalAA(self):
        return str(self.aa_spent + self.aa_avail)
    def __str__(self):
        return self.name
