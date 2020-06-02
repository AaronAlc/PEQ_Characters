from django.db import models

from django.apps import apps

# Create your models here.

class Epic(models.Model):
    epic = models.OneToOneField('characters.Character', on_delete=models.CASCADE)
    epic_complete = models.BooleanField()

    class Meta:
        abstract = True

class Epic_1_5_PreQuest(Epic):
    epic_complete = models.BooleanField(default=False, verbose_name="Epic 1.5 Complete?")

    class Meta:
        abstract = True

class War_Epic_1_5_PreQuest(Epic_1_5_PreQuest):
    epic_1_5_prequest_step1 = models.BooleanField(default=False, verbose_name="Kill Diaku Overseer and loot Korbuk's weapon plans")
    epic_1_5_prequest_step2 = models.BooleanField(default=False, verbose_name="Hello World")
