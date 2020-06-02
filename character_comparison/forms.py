from django import forms

from characters.models import Character
from armor.models import EquipArmorSlot

class CharacterGearComparison(forms.Form):
    classes = forms.MultipleChoiceField(choices=Character.CHAR_CLASSES, required=False, widget=forms.CheckboxSelectMultiple())
    slots = forms.MultipleChoiceField(choices=EquipArmorSlot.EQUIP_SLOTS, required=False, widget=forms.CheckboxSelectMultiple())
    char_sets = forms.MultipleChoiceField(choices=Character.CHAR_SETS, required=False, widget=forms.CheckboxSelectMultiple())

    def render(self, *args, **kwargs):
        output = super(CharacterGearComparison, self).render(*args, **kwargs)
        return mark_safe(output.replace(u'<ul>', u'').replace(u'</ul>', u'').replace(u'<li>', '<p>').replace(u'</li>', u'</p>'))
