# Generated by Django 5.0.6 on 2024-07-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0005_remove_profile_friend'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friend',
            field=models.ManyToManyField(related_name='amigo', to='mychatapp.friends'),
        ),
    ]
