# Generated by Django 3.1.3 on 2021-02-13 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('afflictions', '0001_initial'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sicknessexamination',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sicknesses', to='core.examination', verbose_name='badanie'),
        ),
        migrations.AddField(
            model_name='sicknessexamination',
            name='sickness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='examinations', to='afflictions.sickness', verbose_name='choroba'),
        ),
        migrations.AddField(
            model_name='sickness',
            name='afflictions',
            field=models.ManyToManyField(related_name='sicknesses', to='afflictions.Affliction', verbose_name='objawy'),
        ),
        migrations.AddField(
            model_name='parasite',
            name='afflictions',
            field=models.ManyToManyField(related_name='parasites', to='afflictions.Affliction', verbose_name='objawy'),
        ),
        migrations.AddField(
            model_name='medicineexamination',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicines', to='core.examination', verbose_name='badanie'),
        ),
        migrations.AddField(
            model_name='medicineexamination',
            name='medicine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='examinations', to='afflictions.medicine', verbose_name='lek'),
        ),
        migrations.AddField(
            model_name='fungusexamination',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fungi', to='core.examination', verbose_name='badanie'),
        ),
        migrations.AddField(
            model_name='fungusexamination',
            name='fungus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='examinations', to='afflictions.fungus', verbose_name='grzyb'),
        ),
        migrations.AddField(
            model_name='fungus',
            name='afflictions',
            field=models.ManyToManyField(related_name='fungi', to='afflictions.Affliction', verbose_name='objawy'),
        ),
    ]