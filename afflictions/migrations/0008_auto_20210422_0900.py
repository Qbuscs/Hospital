# Generated by Django 3.1.3 on 2021-04-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afflictions', '0007_auto_20210422_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='parasite',
            name='subtype',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='sub-typ'),
        ),
        migrations.AlterField(
            model_name='parasite',
            name='species',
            field=models.CharField(max_length=200, verbose_name='gatunek'),
        ),
        migrations.AlterUniqueTogether(
            name='parasite',
            unique_together={('species', 'subtype')},
        ),
    ]
