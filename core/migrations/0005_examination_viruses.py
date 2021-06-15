# Generated by Django 3.1.3 on 2021-06-14 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afflictions', '0012_auto_20210614_0252'),
        ('core', '0004_auto_20210422_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='examination',
            name='viruses',
            field=models.ManyToManyField(blank=True, related_name='examinations', to='afflictions.Virus', verbose_name='wirusy'),
        ),
    ]