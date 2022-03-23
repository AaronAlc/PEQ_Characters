from django.db import models

# Create your models here.
import characters.models
import epic_tracker.models

class EpicStatus(models.Model):
    character = models.OneToOneField('characters.Character', on_delete=models.CASCADE, default=None)
    epic_1_0_complete = models.BooleanField(default=False, verbose_name="Epic 1.0 Complete?")
    epic_1_5_complete = models.BooleanField(default=False, verbose_name="Epic 1.5 Complete?")
    epic_1_5_pre_complete = models.BooleanField(default=False, verbose_name="Epic 1.5 Pre Quest Complete?")
    epic_2_0_complete = models.BooleanField(default=False, verbose_name="Epic 2.0 Complete?")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, **kwargs):
        super(EpicStatus, self).save(**kwargs)
        characterClass = self.character.char_class
        if characterClass == characters.models.Character.WARRIOR:
            epic_tracker.models.War_Epic_1_5_PreQuest_Step.objects.get_or_create(epic_status=self)
            epic_tracker.models.War_Epic_1_5_Step.objects.get_or_create(epic_status=self)
            epic_tracker.models.War_Epic_2_0_Step.objects.get_or_create(epic_status=self)
        elif characterClass == characters.models.Character.WIZARD:
            pass

    def __str__(self):
        return self.character.name

    def return_character(self):
        return self.character

    class Meta:
        db_table = 'Epic_Status'
        verbose_name_plural = 'Epic Statuses'


