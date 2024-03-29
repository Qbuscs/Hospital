# Generated by Django 3.1.3 on 2021-03-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travels', '0002_auto_20210218_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='drinks',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'butelkowane'), (1, 'lokalne'), (2, 'strumienie'), (3, 'mieszane')], null=True, verbose_name='napoje'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='food',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'restauracje'), (1, 'lokalne'), (2, 'własne'), (3, 'mieszane')], null=True, verbose_name='odżywianie'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='visit',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'zawodowy'), (1, 'turystyczny')], null=True, verbose_name='rodzaj wizyty'),
        ),
    ]
