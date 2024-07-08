# Generated by Django 5.0.6 on 2024-07-07 05:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mychatapp', '0017_chatmessage_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
