# Generated by Django 4.2.5 on 2023-09-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='yearend',
            field=models.IntegerField(default=2023),
        ),
        migrations.AddField(
            model_name='events',
            name='yearstart',
            field=models.IntegerField(default=2023),
        ),
    ]
