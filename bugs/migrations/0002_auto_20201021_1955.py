# Generated by Django 3.1.2 on 2020-10-21 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='class_name',
            field=models.CharField(blank=True, default='General', max_length=100),
        ),
        migrations.AddField(
            model_name='bugs',
            name='state',
            field=models.CharField(default='open', max_length=100),
        ),
    ]