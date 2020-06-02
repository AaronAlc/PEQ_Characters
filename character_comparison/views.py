from django.shortcuts import render
from armor.models import EquipArmorSlot, Armor
from characters.models import Character
from django.db.models import Q
from character_comparison.forms import CharacterGearComparison

#Create your views here.
def index(request):
    try:
        eas = EquipArmorSlot.objects.order_by('current_equip_slot', 'character__char_class', '-armor__hp_points')
    except:
        eas = None
        if eas is not None:
            return render(request, 'index.html', {'eas' : eas})
    return render(request, 'index.html', {'eas' : eas})

def search(request):
    form = CharacterGearComparison(request.GET)
    if request.method == 'GET':
        if form.is_valid():
            eas = EquipArmorSlot.objects.all()
#get data from form
            data = form.cleaned_data
            classes = data.get('classes')
            slots = data.get('slots')
            char_sets = data.get('char_sets')
            char_set_query = []
            for sets in char_sets:
                lookup = Character.CHAR_SETS_LOOK_UP[sets]
                for c in lookup:
                    if c not in char_set_query:
                        char_set_query.append(c)

            if len(classes) > 0:
                eas = eas.filter(character__char_class__in=classes)
            if len(slots) > 0:
                eas = eas.filter(current_equip_slot__in=slots)
            if len(char_set_query) > 0:
                eas = eas.filter(character__char_class__in=char_set_query)
            if len(slots) == 1:
                eas = eas.order_by('armor__hp_points')
            else:
                eas = eas.order_by('armor__hp_points', 'character')
            return render(request, 'comparison_search.html', {'form' : form, 'eas' : eas})
    else:
        form = CharacterGearComparison()
    return render(request, 'comparison_view.html', {'form' : form})
