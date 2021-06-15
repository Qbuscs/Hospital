# Generated by Django 3.1.3 on 2021-06-14 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afflictions', '0011_auto_20210612_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Getunek')),
            ],
            options={
                'verbose_name': 'wirus',
                'verbose_name_plural': 'wirus',
            },
        ),
        migrations.AlterModelOptions(
            name='bacteriaexamination',
            options={'verbose_name': 'bakteria w badaniu', 'verbose_name_plural': 'bakterie w badaniu'},
        ),
        migrations.AlterField(
            model_name='bacteria',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Gatunek'),
        ),
    ]