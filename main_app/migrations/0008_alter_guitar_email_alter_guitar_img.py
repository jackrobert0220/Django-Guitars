# Generated by Django 4.0.3 on 2022-04-10 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_guitar_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guitar',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='guitar',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
