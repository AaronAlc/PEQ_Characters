# Generated by Django 2.1.4 on 2018-12-17 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('armor_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('armor_class', models.IntegerField(default=0)),
                ('strength', models.IntegerField(default=0)),
                ('stamina', models.IntegerField(default=0)),
                ('agility', models.IntegerField(default=0)),
                ('dexterity', models.IntegerField(default=0)),
                ('wisdom', models.IntegerField(default=0)),
                ('intelligence', models.IntegerField(default=0)),
                ('charisma', models.IntegerField(default=0)),
                ('hp_points', models.IntegerField(default=0)),
                ('mana_points', models.IntegerField(default=0)),
                ('endurance_points', models.IntegerField(default=0)),
                ('spell_shielding', models.IntegerField(default=0)),
                ('shieldling', models.IntegerField(default=0)),
                ('focus_effect', models.CharField(blank=True, default=None, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EquipArmorSlot',
            fields=[
                ('equip_slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('current_equip_slot', models.CharField(blank=True, choices=[('slot0', 'Charm'), ('slot1', 'LeftEar'), ('slot2', 'Head'), ('slot3', 'Face'), ('slot4', 'RightEar'), ('slot5', 'Neck'), ('slot6', 'Shoulder'), ('slot7', 'Arms'), ('slot8', 'Back'), ('slot9', 'LeftWrist'), ('slot10', 'RightWrist'), ('slot11', 'Range'), ('slot12', 'Hands'), ('slot13', 'Primary'), ('slot14', 'Secondary'), ('slot15', 'LeftFinger'), ('slot16', 'RightFinger'), ('slot17', 'Chest'), ('slot18', 'Legs'), ('slot19', 'Feet'), ('slot20', 'Waist'), ('slot21', 'Ammo'), ('slot22', 'PowerSource')], default=None, max_length=6, null=True)),
                ('armor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armor.Armor')),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.Character')),
            ],
        ),
        migrations.CreateModel(
            name='WearableArmorSlot',
            fields=[
                ('wear_slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('wearable_armor_slot', models.CharField(blank=True, choices=[('Charm', 'Charm'), ('Ears', 'Ears'), ('Head', 'Head'), ('Face', 'Face'), ('Neck', 'Neck'), ('Shoulders', 'Shoulders'), ('Arms', 'Arms'), ('Back', 'Back'), ('Wrists', 'Wrists'), ('Range', 'Range'), ('Hands', 'Hands'), ('Primary', 'Primary'), ('Secondary', 'Secondary'), ('Fingers', 'Fingers'), ('Chest', 'Chest'), ('Legs', 'Legs'), ('Feet', 'Feet'), ('Waist', 'Waist'), ('Ammo', 'Ammo'), ('PowerSource', 'PowerSource')], default=None, max_length=15)),
                ('armor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='armor.Armor')),
            ],
        ),
    ]
