# Generated by Django 3.1.3 on 2021-03-08 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0003_auto_20210223_2324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Morphology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Nazwa')),
                ('unit', models.CharField(max_length=32, verbose_name='Jednostka')),
                ('norm_min', models.FloatField(blank=True, null=True, verbose_name='Norma dolna')),
                ('norm_max', models.FloatField(blank=True, null=True, verbose_name='Norma górna')),
            ],
            options={
                'verbose_name': 'Badanie morfologiczne',
                'verbose_name_plural': 'Badania morfologiczne',
            },
        ),
        migrations.CreateModel(
            name='MorphologyExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField(verbose_name='Wyniki')),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examination', verbose_name='Badanie')),
                ('morphology', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='morphologies.morphology', verbose_name='Badanie morfologiczne')),
            ],
            options={
                'unique_together': {('morphology', 'examination')},
            },
        ),
    ]