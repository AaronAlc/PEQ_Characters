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
    char_id = models.AutoField(primary_key=True)
    char_class = models.CharField(max_length=3, choices=CHAR_CLASSES)
    name = models.CharField(max_length=30)
    level = models.IntegerField()
    def __str__(self):
        return self.name
