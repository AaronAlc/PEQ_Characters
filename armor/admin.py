from django.contrib import admin
from .models import Armor, EquipArmorSlot, WearableArmorSlot

# Register your models here.
admin.site.register(Armor)
admin.site.register(EquipArmorSlot)
admin.site.register(WearableArmorSlot)
#admin.site.register(Equipped_Armor_Slot)
