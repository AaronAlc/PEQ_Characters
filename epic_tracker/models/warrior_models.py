from django.db import models

import characters.models
from epic_tracker.models import EpicStatus


class War_Epic_2_0_Step(models.Model):
    epic_status = models.OneToOneField('epic_tracker.EpicStatus', on_delete=models.CASCADE, default=None)
    step1 = models.BooleanField(default=False, verbose_name="Dranik Scak: Say 'going back' to Korbuk Brimblade")
    step2 = models.BooleanField(default=False, verbose_name="MPG: Kill Possesed Brute Loot Krejinok's Muddled Rage ")
    step3 = models.BooleanField(default=False, verbose_name="Dranik Scar: Hand in Krejinok's Muddled Rage")
    step4 = models.BooleanField(default=False, verbose_name="Iceclad: Locate Frozen Pestle +1070, +5225")
    step5 = models.BooleanField(default=False, verbose_name="Iceclad: Hand in Frozen Pestle to Fazzle")
    step6 = models.BooleanField(default=False, verbose_name="Iceclad: Say 'map' to Fazzle")
    step7 = models.BooleanField(default=False,
                                verbose_name="Eastern Wastes: Find and Kill Larnik. Loot Purification Kit")
    step8 = models.BooleanField(default=False,
                                verbose_name="Dranik Scar: Combine Muddled Rage in kit to craft Focused Rage")
    step9 = models.BooleanField(default=False, verbose_name="CoA: Loot Globe of Discordant Energy")
    step10 = models.BooleanField(default=False, verbose_name="Dranik Scar: Hand in Globe to Korbuk")
    step11 = models.BooleanField(default=False,
                                 verbose_name="Dranik Scar: Hand in Focused Rage and Champion's Sword of Eternal Power")
    step12 = models.BooleanField(default=False, verbose_name="NC: Slay Korbuk/Kreljnok.Loot Essence and Scabbard")
    step13 = models.BooleanField(default=False, verbose_name="Combine Essenceand 1.5 in Scabbard to form 2.0")

    class Meta:
        db_table = "Warrior_2_0_Epic_Step"


class War_Epic_1_5_Step(models.Model):
    epic_status = models.OneToOneField('epic_tracker.EpicStatus', on_delete=models.CASCADE, default=None)
    epic_1_5_first_vision = models.BooleanField(default=False)
    epic_1_5_step1 = models.BooleanField(default=False,
                                         verbose_name="Draniks Scar: Loot pages and cover, turn into Korbuk")
    epic_1_5_step2 = models.BooleanField(default=False,
                                         verbose_name="Abysmal Sea: Turn in pages and cover to Rewina Jalmoy.")
    epic_1_5_step3 = models.BooleanField(default=False, verbose_name="Receive Recounted History of War")
    epic_1_5_second_vision = models.BooleanField(default=False)
    epic_1_5_step4 = models.BooleanField(default=False,
                                         verbose_name="Draniks Scar: Turn in Recounted History of War to Korbuk")
    epic_1_5_step5 = models.BooleanField(default=False, verbose_name="Receive Energy Receptor")
    epic_1_5_step6 = models.BooleanField(default=False, verbose_name="Find Blackfall Ore")
    epic_1_5_third_vision = models.BooleanField(default=False)
    epic_1_5_step7 = models.BooleanField(default=False, verbose_name="Draniks Scar: Give Blackfall Ore to Korbuk")
    epic_1_5_step8 = models.BooleanField(default=False, verbose_name="Receive Smelting Plans")
    epic_1_5_step9 = models.BooleanField(default=False,
                                         verbose_name="Nedarias Landing: Find iksar blacksmith, turn in 7 flasks of water")
    epic_1_5_step10 = models.BooleanField(default=False, verbose_name="PLACEHOLDER**")
    epic_1_5_step11 = models.BooleanField(default=False, verbose_name="Receive Blackfall Blade")
    epic_1_5_fourth_vision = models.BooleanField(default=False)
    epic_1_5_step12 = models.BooleanField(default=False, verbose_name="Draniks Scar: Turn in Blackfall Blade to Korbuk")
    epic_1_5_step13 = models.BooleanField(default=False, verbose_name="Receive hidden flag for Vxed")
    epic_1_5_step14 = models.BooleanField(default=False,
                                          verbose_name="Vxed: Kill all three Borerlings, spawn Blackfall Borer")
    epic_1_5_step15 = models.BooleanField(default=False, verbose_name="Loot Vial of Blackfall Blood")
    epic_1_5_fifth_vision = models.BooleanField(default=False)
    epic_1_5_step16 = models.BooleanField(default=False,
                                          verbose_name="Draniks Scar:Turn in Vial of Blackfall Blood to Korbuk")
    epic_1_5_step17 = models.BooleanField(default=False, verbose_name="Receive Sealed Vial of Blackfall Blood")
    epic_1_5_step18 = models.BooleanField(default=False,
                                          verbose_name="Everfrost: Find Kimber Whitefoot, turn Sealed Vial of Blackfall Blood.")
    epic_1_5_step19 = models.BooleanField(default=False,
                                          verbose_name="Everfrost: Wait near Permafrost for Kikber to return")
    epic_1_5_step20 = models.BooleanField(default=False, verbose_name="Receive Potion of the Blackfall Spirit")
    epic_1_5_sixth_vision = models.BooleanField(default=False)
    epic_1_5_step21 = models.BooleanField(default=False,
                                          verbose_name="Draniks Scar: Turn Potion of the Blackfall Spirit into Korbuk")
    epic_1_5_step22 = models.BooleanField(default=False, verbose_name="Bloodfields: Kill Girplan Devourer")
    epic_1_5_step23 = models.BooleanField(default=False, verbose_name="Loot Decrepit Hilt")
    epic_1_5_step24 = models.BooleanField(default=False, verbose_name="Draniks Scar:Turn in Decrepit Hilt to Korbuk")
    epic_1_5_step25 = models.BooleanField(default=False,
                                          verbose_name="Firiona Vie: Find Corfia Nultethen, must speak elder elvish")
    epic_1_5_step26 = models.BooleanField(default=False, verbose_name="Turn in Platinum Bar")
    epic_1_5_step27 = models.BooleanField(default=False, verbose_name="Turn in Nocturnal Mask of Acuity")
    epic_1_5_step28 = models.BooleanField(default=False, verbose_name="Turn in Decrepit Hilt")
    epic_1_5_step29 = models.BooleanField(default=False, verbose_name="Veksar: Kill Galuk Drek")
    epic_1_5_step30 = models.BooleanField(default=False, verbose_name="Loot Skeletal Tome of Galuk Drek")
    epic_1_5_step31 = models.BooleanField(default=False, verbose_name="Firiona Vie: Turn in Tome to Corfia")
    epic_1_5_step32 = models.BooleanField(default=False, verbose_name="Receive Glistening Hilt")
    epic_1_5_seventh_vision = models.BooleanField(default=False)
    epic_1_5_step33 = models.BooleanField(default=False, verbose_name="Draniks Scar: Turn in Glistening Hilt to Korbuk")
    epic_1_5_step34 = models.BooleanField(default=False, verbose_name="Loot Stones of Eternal Power")
    epic_1_5_step35 = models.BooleanField(default=False, verbose_name="Walls of Slaughter: Dragorn Campion")
    epic_1_5_step36 = models.BooleanField(default=False, verbose_name="Nobles Causeway: Ground Spawn")
    epic_1_5_step37 = models.BooleanField(default=False, verbose_name="Muramite Proving Grounds: Ground Spawn")
    epic_1_5_step38 = models.BooleanField(default=False, verbose_name="Bloodfields: Ground Spawn")
    epic_1_5_step39 = models.BooleanField(default=False, verbose_name="Draniks Scar: Turn in stones to Korbuk")
    epic_1_5_step40 = models.BooleanField(default=False, verbose_name="Butcherblock: Turn in stones to Gridbar")
    epic_1_5_step41 = models.BooleanField(default=False,
                                          verbose_name="Butcherblock: Turn in Gemming Tool and Spell: Fire to Gridbar")
    epic_1_5_step42 = models.BooleanField(default=False,
                                          verbose_name="Butcherblock: Turn in Glistening Hilt to Gridbar")
    epic_1_5_step43 = models.BooleanField(default=False, verbose_name="Receive Carved Keg Stamp")
    epic_1_5_step44 = models.BooleanField(default=False, verbose_name="Shadow Haven: Turn in Stamp to Koren Galund")
    epic_1_5_step45 = models.BooleanField(default=False, verbose_name="Receive Tube of Setting Solution")
    epic_1_5_step46 = models.BooleanField(default=False,
                                          verbose_name="Butcherblock: Turn in Setting Solution to Gridbar")
    epic_1_5_step47 = models.BooleanField(default=False, verbose_name="Receive Hilt of Eternal Power")
    epic_1_5_eigth_vision = models.BooleanField(default=False)
    epic_1_5_step48 = models.BooleanField(default=False,
                                          verbose_name="Draniks Scar: Turn in Hilt of Eternal Power to Korbuk")
    epic_1_5_step49 = models.BooleanField(default=False,
                                          verbose_name="Ruined City of Dranik: Give Krekk Brimblade the Blackfall Blade, Potion of Blackfall Blood and Hilt of Eternal Power")
    epic_1_5_step50 = models.BooleanField(default=False, verbose_name="Ruined City of Dranik: Kill Krekk and Loot 1.5")

    class Meta:
        db_table = "Warrior_1_5_Epic_Step"

class War_Epic_1_5_PreQuest_Step(models.Model):
    epic_status = models.OneToOneField('epic_tracker.EpicStatus', on_delete=models.CASCADE, default=None)
    epic_1_5_prequest_step1 = models.BooleanField(default=False,
                                                  verbose_name="Kill Diaku Overseer and loot Korbuk's weapon plans")
    epic_1_5_prequest_step2 = models.BooleanField(default=False,
                                                  verbose_name="Kill Shoqui the forggen for an Elegant Shank")
    epic_1_5_prequest_step3 = models.BooleanField(default=False,
                                                  verbose_name="Turn in Korbuk's Weapon Plans (you get plans back)")
    epic_1_5_prequest_step4 = models.BooleanField(default=False,
                                                  verbose_name="Kill Drevlon and loot the Redblade Family Sword")
    epic_1_5_prequest_step5 = models.BooleanField(default=False,
                                                  verbose_name="Turn in Redblade Family Sword to Kargrek (he gives you Emblazoned Champion's Hilt)")
    epic_1_5_prequest_step6 = models.BooleanField(default=False, verbose_name="Turn in Hilt to Korbuk")
    epic_1_5_prequest_step7 = models.BooleanField(default=False,
                                                  verbose_name="Craft Coldain Coffee Blend for Dardek Bladewright in Thurgadin")
    epic_1_5_prequest_step8 = models.BooleanField(default=False,
                                                  verbose_name="Turn in Korbuk's Weapon Plans and the Elegant Shank and Hilt to Dardek (you receive Darkdek's Forged Blade)")
    epic_1_5_prequest_step9 = models.BooleanField(default=False, verbose_name="Turn in Dardek's Forged Blade to Korbuk")
    epic_1_5_prequest_step10 = models.BooleanField(default=False, verbose_name="You receive Korbuk's Blade of Mastery")

    class Meta:
        db_table = "Warrior_1_5_PreQuest_Epic_Step"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, **kwargs):

        epicStatus = EpicStatus.objects.get(pk=self.epic_status_id)
        if (epicStatus.character.char_class == characters.models.Character.WARRIOR):
            super(War_Epic_1_5_PreQuest_Step, self).save(**kwargs)
            if (self.epic_1_5_prequest_step10):
                epicStatus = EpicStatus.objects.get(pk=self.epic_status_id)
                epicStatus.epic_1_5_pre_complete = True
                epicStatus.save()

    def __str__(self):
        return str(self.epic_status)
