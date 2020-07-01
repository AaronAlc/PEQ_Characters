from django.core.management import BaseCommand
from django.core.management import CommandError

from characters.models import Character
from characters.services.CharacterService import update_character


class Command(BaseCommand):
	help = 'Updates a Character by pulling from ProjectEQ Magelo'

	def add_arguments(self, parser):
		parser.add_argument('characters', nargs='+', type=str)

	def handle(self, *args, **options):
		for character_name in options['characters']:
			try:
				character = Character.objects.get(name=character_name)
			except Character.DoesNotExist:
				raise CommandError('Character %s does not exist' % character_name)
			update_character(character.name)

