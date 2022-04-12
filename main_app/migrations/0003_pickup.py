# Generated by Django 4.0.3 on 2022-04-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_guitar_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pickup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('active', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3)),
            ],
        ),
    ]
