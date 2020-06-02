from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Character
from armor.models import Armor, EquipArmorSlot, Augmentation
from characters.scripts.updateArmor import getCharacterMagelo

#Create your views here.
def index(request):
    character_list = Character.objects.all().order_by('aa_spent')
    context = {'character_list': character_list}
    if (request.method == ('POST')):
        for char in character_list:
            getCharacterMagelo(char.name)
        return HttpResponseRedirect('/characters/')
    return render(request, 'characters/index.html', context)

def detail(request, name):
    character = get_object_or_404(Character, name=name)
    try:
        eas = EquipArmorSlot.objects.filter(character=character)
    except:
        eas = None
    if eas is not None:
        missingAnguishAugs = Augmentation.ANGUISH_AUG_NAMES
        qs = eas.filter(aug1__aug__name__in=Augmentation.ANGUISH_AUG_NAMES)
        for q in qs:
            if q.aug1.aug.name in missingAnguishAugs: 
                missingAnguishAugs.remove(q.aug1.aug.name)
        return render(request, 'characters/detail.html', {'character': character, 'eas' : eas, 'missingAnguishAugs' : missingAnguishAugs})
    return render(request, 'characters/detail.html', {'character': character})

def update_db(request):
    return render_to_response(request, 'characters/index.html')

