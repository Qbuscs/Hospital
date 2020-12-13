# Generated by Django 3.1.3 on 2020-12-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afflictions', '0004_auto_20201109_2109'),
        ('core', '0006_auto_20201109_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='afflictions',
            field=models.ManyToManyField(blank=True, related_name='examinations', to='afflictions.Affliction', verbose_name='objawy'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='parasites',
            field=models.ManyToManyField(blank=True, related_name='examinations', to='afflictions.Parasite', verbose_name='pasożyty'),
        ),
    ]
