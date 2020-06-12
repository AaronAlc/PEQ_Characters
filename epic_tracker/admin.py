from django.contrib import admin

from .models import War_1_5_Epic, War_1_5_Epic_PreQuest, War_2_0_Epic
# Register your models here.

admin.site.register(War_1_5_Epic_PreQuest)
admin.site.register(War_1_5_Epic)
admin.site.register(War_2_0_Epic)

