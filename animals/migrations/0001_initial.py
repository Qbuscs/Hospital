# Generated by Django 3.1.3 on 2021-02-13 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nazwa')),
            ],
            options={
                'verbose_name': 'zwierzę',
                'verbose_name_plural': 'zwierzęta',
            },
        ),
        migrations.CreateModel(
            name='AnimalExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.PositiveSmallIntegerField(choices=[(0, 'zawodowe'), (1, 'domowe'), (2, 'inne')], verbose_name='kontakt')),
                ('saliva', models.BooleanField(blank=True, null=True, verbose_name='kontakt ze śliną')),
                ('excrement', models.BooleanField(blank=True, null=True, verbose_name='kontakt z odchodami')),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.animal', verbose_name='zwierzę')),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='core.examination')),
            ],
            options={
                'verbose_name': 'Kontakt ze zwierzęciem',
                'verbose_name_plural': 'Kontakty ze zwierzętami',
            },
        ),
    ]
