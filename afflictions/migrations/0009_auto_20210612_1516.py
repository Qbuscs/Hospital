# Generated by Django 3.1.3 on 2021-06-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afflictions', '0008_auto_20210422_0900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fungus',
            name='antibiotics_resistance',
        ),
        migrations.AddField(
            model_name='fungusexamination',
            name='high_resistance',
            field=models.ManyToManyField(related_name='fungus_examination_high_resistance', to='afflictions.Medicine', verbose_name='oporny na'),
        ),
        migrations.AddField(
            model_name='fungusexamination',
            name='low_resistance',
            field=models.ManyToManyField(related_name='fungus_examination_low_resistance', to='afflictions.Medicine', verbose_name='wrażliwy na'),
        ),
        migrations.AddField(
            model_name='fungusexamination',
            name='mid_resistance',
            field=models.ManyToManyField(related_name='fungus_examination_mid_resistance', to='afflictions.Medicine', verbose_name='średnio wrażliwy na'),
        ),
        migrations.AlterField(
            model_name='fungus',
            name='afflictions',
            field=models.ManyToManyField(blank=True, related_name='fungi', to='afflictions.Affliction', verbose_name='objawy'),
        ),
        migrations.AlterField(
            model_name='fungusexamination',
            name='amount',
            field=models.FloatField(verbose_name='ilość'),
        ),
        migrations.AlterField(
            model_name='parasite',
            name='afflictions',
            field=models.ManyToManyField(blank=True, null=True, related_name='parasites', to='afflictions.Affliction', verbose_name='objawy'),
        ),
    ]
