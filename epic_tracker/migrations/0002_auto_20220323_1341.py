# Generated by Django 2.1.4 on 2022-03-23 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epic_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='war_epic_1_5_prequest_step',
            table='Warrior_1_5_PreQuest_Epic_Step',
        ),
        migrations.AlterModelTable(
            name='war_epic_1_5_step',
            table='Warrior_1_5_Epic_Step',
        ),
        migrations.AlterModelTable(
            name='war_epic_2_0_step',
            table='Warrior_2_0_Epic_Step',
        ),
    ]
