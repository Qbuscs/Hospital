# Generated by Django 3.1.3 on 2021-02-18 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210218_1859'),
        ('travels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='travels', to='core.examination'),
        ),
    ]
