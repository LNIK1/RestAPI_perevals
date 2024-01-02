# Generated by Django 5.0 on 2024-01-02 07:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PerevalAdded',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=255, verbose_name='Индекс')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('other_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Другое название')),
                ('connect', models.TextField(blank=True, null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('NW', 'New'), ('AC', 'Accepted'), ('PN', 'Pending'), ('RJ', 'Rejected')], default='NW', max_length=2)),
            ],
            options={
                'verbose_name': 'Перевал',
                'verbose_name_plural': 'Перевалы',
            },
        ),
        migrations.CreateModel(
            name='PerevalCoordinate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(max_length=30, verbose_name='Широта')),
                ('longitude', models.FloatField(max_length=30, verbose_name='Долгота')),
                ('height', models.FloatField(max_length=20, verbose_name='Высота')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б')], max_length=2, null=True, verbose_name='Зима')),
                ('summer', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б')], max_length=2, null=True, verbose_name='Лето')),
                ('autumn', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б')], max_length=2, null=True, verbose_name='Осень')),
                ('spring', models.CharField(blank=True, choices=[('1a', '1A'), ('1b', '1Б'), ('2a', '2А'), ('2b', '2Б'), ('3a', '3А'), ('3b', '3Б'), ('4a', '4А'), ('4b', '4Б'), ('5a', '5А'), ('5b', '5Б')], max_length=2, null=True, verbose_name='Весна')),
            ],
        ),
        migrations.CreateModel(
            name='PerevalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('otc', models.CharField(max_length=255, verbose_name='Отчество')),
                ('email', models.CharField(max_length=255, verbose_name='Почта')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название')),
                ('data', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Название')),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Pereval.perevaladded')),
            ],
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='coord',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Pereval.perevalcoordinate'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pereval.perevallevel'),
        ),
        migrations.AddField(
            model_name='perevaladded',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pereval.perevaluser'),
        ),
    ]