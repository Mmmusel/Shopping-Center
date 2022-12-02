# Generated by Django 3.2.9 on 2022-11-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_auto_20221130_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_address',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_avatar',
            field=models.ImageField(null=True, upload_to='user_avatar/'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_mobile',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
    ]
