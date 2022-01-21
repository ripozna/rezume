# Generated by Django 3.2.6 on 2021-12-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='date_of_birth',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='info',
            name='language',
            field=models.CharField(choices=[('ENG', 'ENGLISH'), ('RU', 'RUSSIAN')], max_length=3),
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='info',
            name='phone_number',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='info',
            name='surname',
            field=models.CharField(max_length=40),
        ),
    ]
