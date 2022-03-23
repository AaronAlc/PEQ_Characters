from django.contrib import admin

from epic_tracker.models.warrior_models import War_Epic_1_5_PreQuest_Step, War_Epic_1_5_Step, War_Epic_2_0_Step
from epic_tracker.models.epic_status import EpicStatus

# Register your models here.

admin.site.register(EpicStatus)
admin.site.register(War_Epic_1_5_PreQuest_Step)
admin.site.register(War_Epic_1_5_Step)
admin.site.register(War_Epic_2_0_Step)
