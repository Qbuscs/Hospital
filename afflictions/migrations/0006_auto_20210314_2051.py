# Generated by Django 3.1.3 on 2021-03-14 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afflictions', '0005_auto_20210314_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fungus',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nazwa'),
        ),
    ]