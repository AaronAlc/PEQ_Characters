from django.db import models


class Wiz_Epic_1_5_PreQuest_Steps(models.Model):
    epic_1_5_prequest_step1 = models.BooleanField(default=False, verbose_name="DO wizard stuff")
    epic_1_5_prequest_step2 = models.BooleanField(default=False, verbose_name="Hello World")
