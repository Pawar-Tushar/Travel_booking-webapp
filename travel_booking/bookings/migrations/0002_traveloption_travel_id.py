# Generated by Django 5.2.4 on 2025-07-06 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveloption',
            name='travel_id',
            field=models.CharField(default='r', editable=False, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
