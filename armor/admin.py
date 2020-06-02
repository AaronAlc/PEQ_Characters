from django.contrib import admin
from .models import Armor, WearableArmorSlot, Augmentation, EquipAugmentation1, EquipAugmentation2, EquipArmorSlot

class EquipArmorSlotAdmin(admin.ModelAdmin):
    list_display = ('character', 'current_equip_slot', 'armor', 'aug1', 'aug2')
    fields = ('current_equip_slot', 'character', 'armor', 'aug1', 'aug2')

# Register your models here.
admin.site.register(Armor)
admin.site.register(EquipArmorSlot, EquipArmorSlotAdmin)
admin.site.register(WearableArmorSlot)
admin.site.register(Augmentation)
admin.site.register(EquipAugmentation1)
admin.site.register(EquipAugmentation2)
