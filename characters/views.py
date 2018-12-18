from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Character
from armor.models import Armor, EquipArmorSlot
from characters.scripts.updateArmor import getCharacterMagelo

# Create your views here.
def index(request):
    character_list = Character.objects.all()
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
    return render(request, 'characters/detail.html', {'character': character, 'eas' : eas})
    #return render(request, 'characters/detail.html', {'character': character})

def update_db(request):
    return render_to_response(request, 'characters/index.html')

def characters_armor_view(request):
    try:
        eas = EquipArmorSlot.objects.all()
    except:
        eas = None
    return render(request, 'characters/comparison_view.html', {'character': character, 'eas' : eas})

