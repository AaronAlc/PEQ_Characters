from django.db import models

from django.apps import apps

# Create your models here.
from characters.models import Character

class Epic(models.Model):
    character_epic = models.OneToOneField(Character, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Epic_1_5_PreQuest_Abstract(Epic):
    epic_complete = models.BooleanField(default=False, verbose_name="Epic 1.5 Pre Quest Complete")

    class Meta:
        abstract = True


class Epic_1_5_Abstract(Epic):
    epic_complete = models.BooleanField(default=False, verbose_name="Epic 1.5 Quest Complete")

    class Meta:
        abstract = True


class Epic_2_0_Abstract(Epic):
    epic_complete = models.BooleanField(default=False, verbose_name="Epic 2.0 Quest Complete")

    class Meta:
        abstract = True


# Warrior
class Warrior_Epic(Epic):
    character_epic = models.OneToOneField(Character, on_delete=models.CASCADE,
                                          limit_choices_to={"char_class": 'WAR'}, blank=False)

    class Meta:
        abstract = True


class War_1_5_Epic_PreQuest(Warrior_Epic, Epic_1_5_PreQuest_Abstract):
    epic_1_5_prequest_step1 = models.BooleanField(default=False,
                                                  verbose_name="Kill Diaku Overseer and loot Korbuk's weapon plans")
    epic_1_5_prequest_step2 = models.BooleanField(default=False, verbose_name="Hello World")


class War_1_5_Epic(Warrior_Epic, Epic_1_5_Abstract):
    pass


class War_2_0_Epic(Warrior_Epic, Epic_2_0_Abstract):
    pass

# Shaman
class Shaman_Epic(Epic):
    character_epic = models.OneToOneField(Character, on_delete=models.CASCADE,
                                          limit_choices_to={"char_class": 'SHM'}, blank=False)
    class Meta:
        abstract = True

class Shm_1_5_Epic_PreQuest(Shaman_Epic, Epic_1_5_PreQuest_Abstract):
    pass

class Shm_1_5_Epic(Shaman_Epic, Epic_1_5_Abstract):
    pass

class Shm_2_0_Epic(Shaman_Epic, Epic_2_0_Abstract):
    pass
