# Generated by Django 3.1.3 on 2021-07-20 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_auto_20210612_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalexamination',
            name='skin',
            field=models.BooleanField(blank=True, null=True, verbose_name='kontakt z sierścią / skórą'),
        ),
    ]