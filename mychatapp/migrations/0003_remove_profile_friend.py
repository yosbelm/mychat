# Generated by Django 5.0.6 on 2024-07-03 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0002_profile_friend'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='friend',
        ),
    ]
