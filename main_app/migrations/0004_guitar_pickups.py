# Generated by Django 4.0.3 on 2022-04-02 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_pickup'),
    ]

    operations = [
        migrations.AddField(
            model_name='guitar',
            name='pickups',
            field=models.ManyToManyField(to='main_app.pickup'),
        ),
    ]