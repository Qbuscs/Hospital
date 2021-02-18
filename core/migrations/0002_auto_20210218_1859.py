# Generated by Django 3.1.3 on 2021-02-18 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=30, verbose_name='wiek'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='examination',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='examinations', to='core.patient', verbose_name='pacjent'),
        ),
    ]
