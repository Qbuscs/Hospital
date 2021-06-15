# Generated by Django 3.1.3 on 2021-06-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalexamination',
            name='blood',
            field=models.BooleanField(blank=True, null=True, verbose_name='kontakt z krwią'),
        ),
        migrations.AddField(
            model_name='animalexamination',
            name='scratches',
            field=models.BooleanField(blank=True, null=True, verbose_name='podrapania'),
        ),
    ]