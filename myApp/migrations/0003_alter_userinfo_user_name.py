# Generated by Django 3.2.9 on 2022-11-28 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='user_name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
