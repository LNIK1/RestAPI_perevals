# Generated by Django 5.0 on 2024-01-03 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pereval', '0002_alter_image_options_alter_perevalcoordinate_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perevaladded',
            name='status',
            field=models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Rejected', 'Rejected')], default='New', max_length=8, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='perevaluser',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Телефон'),
        ),
    ]