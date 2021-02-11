# Generated by Django 3.1.3 on 2020-12-29 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20201213_1914'),
        ('afflictions', '0004_auto_20201109_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True, verbose_name='ilość')),
                ('unit', models.CharField(blank=True, max_length=50, null=True, verbose_name='jednostka')),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examination', verbose_name='badanie')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='afflictions.medicine', verbose_name='lek')),
            ],
        ),
    ]