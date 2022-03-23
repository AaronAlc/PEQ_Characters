from django.db import models

# Create your models here.
from epic_tracker.models import EpicStatus


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

    WARRIOR = CHAR_CLASSES[0][0]
    CLERIC = CHAR_CLASSES[1][0]
    PALADIN = CHAR_CLASSES[2][0]
    RANGER = CHAR_CLASSES[3][0]
    SHADOWKNIGHT = CHAR_CLASSES[4][0]
    DRUID = CHAR_CLASSES[5][0]
    BARD = CHAR_CLASSES[6][0]
    ROGUE = CHAR_CLASSES[7][0]
    SHAMAN = CHAR_CLASSES[8][0]
    NECROMANCER = CHAR_CLASSES[9][0]
    WIZARD= CHAR_CLASSES[10][0]
    MAGICIAN = CHAR_CLASSES[11][0]
    ENCHANTER = CHAR_CLASSES[12][0]
    BEASTLORD = CHAR_CLASSES[13][0]
    BERZERKER = CHAR_CLASSES[14][0]
    MONK = CHAR_CLASSES[15][0]

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
        'Silk': ['NEC', 'WIZ', 'MAG', 'ENC'],
        'Chain': ['RNG', 'ROG', 'SHM', 'BER'],
        'Leather': ['DRU', 'BST', 'MNK'],
        'Priests': ['CLR', 'SHM', 'DRU'],
        'Melee': ['WAR', 'PAL', 'RNG', 'SHD', 'BRD', 'ROG', 'BST', 'BER', 'MNK'],
        'Casters': ['CLR', 'DRU', 'SHM', 'NEC', 'WIZ', 'MAG', 'ENC', ],
    }

    char_id = models.AutoField(primary_key=True)
    char_class = models.CharField(max_length=3, choices=CHAR_CLASSES)
    name = models.CharField(max_length=30, unique=True)
    level = models.IntegerField(default=1)
    aa_spent = models.IntegerField(default=0)
    aa_avail = models.IntegerField(default=0)

    def getTotalAA(self):
        return str(self.aa_spent + self.aa_avail)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, **kwargs):
        super(Character, self).save(**kwargs)
        EpicStatus.objects.get_or_create(character=self)
