# Generated by Django 3.1.3 on 2021-03-14 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afflictions', '0003_auto_20210218_1859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fungus',
            old_name='molecular_identification',
            new_name='name',
        ),
    ]
