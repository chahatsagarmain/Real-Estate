# Generated by Django 5.0 on 2023-12-20 00:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='date_hired',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 20, 0, 31, 13, 360387)),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photos/2023-12-20 00:31:13.360287'),
        ),
    ]
