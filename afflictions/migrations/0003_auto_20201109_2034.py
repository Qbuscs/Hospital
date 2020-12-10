# Generated by Django 3.1.3 on 2020-11-09 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20201109_0024'),
        ('afflictions', '0002_auto_20201109_0034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fungus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('molecular_identification', models.TextField(verbose_name='identyfikacja molekularna')),
                ('antibiotics_resistance', models.PositiveSmallIntegerField(choices=[(0, 'niska'), (1, 'średnia'), (2, 'wysoka')], verbose_name='odporność na antybiotyki')),
                ('afflictions', models.ManyToManyField(related_name='fungi', to='afflictions.Affliction', verbose_name='objawy')),
            ],
        ),
        migrations.AlterModelOptions(
            name='sicknessexamination',
            options={'verbose_name': 'Choroba w badaniu', 'verbose_name_plural': 'Choroby w badaniu'},
        ),
        migrations.AlterField(
            model_name='sicknessexamination',
            name='examination',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examination', verbose_name='badanie'),
        ),
        migrations.AlterField(
            model_name='sicknessexamination',
            name='sickness',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='afflictions.sickness', verbose_name='choroba'),
        ),
        migrations.CreateModel(
            name='Parasite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='nazwa')),
                ('afflictions', models.ManyToManyField(related_name='parasites', to='afflictions.Affliction', verbose_name='objawy')),
            ],
        ),
        migrations.CreateModel(
            name='FungusExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='ilość')),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.examination', verbose_name='badanie')),
                ('fungus', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='afflictions.fungus', verbose_name='grzyb')),
            ],
        ),
    ]