import logging

from django.core.management import call_command
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.shortcuts import render_to_response

from armor.models import Augmentation
from armor.models import EquipArmorSlot
from .models import Character

logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
	character_list = Character.objects.all().order_by('aa_spent')
	context = {'character_list': character_list}
	if request.method == 'POST':
		for char in character_list:
			call_command('updatecharacter', char)
		return HttpResponseRedirect('/characters/')
	return render(request, 'characters/index.html', context)


def detail(request, name):
	character = get_object_or_404(Character, name=name)
	try:
		eas = EquipArmorSlot.objects.filter(character=character)
	except EquipArmorSlot.DoesNotExist:
		eas = None
	if eas is not None:
		missing_anguish_augs = Augmentation.ANGUISH_AUG_NAMES
		qs = eas.filter(aug1__aug__name__in=Augmentation.ANGUISH_AUG_NAMES)
		for q in qs:
			if q.aug1.aug.name in missing_anguish_augs:
				missing_anguish_augs.remove(q.aug1.aug.name)
		return render(request, 'characters/detail.html',
		              {'character': character, 'eas': eas, 'missing_anguish_augs': missing_anguish_augs})
	return render(request, 'characters/detail.html', {'character': character})


def update_db(request):
	return render_to_response(request, 'characters/index.html')
