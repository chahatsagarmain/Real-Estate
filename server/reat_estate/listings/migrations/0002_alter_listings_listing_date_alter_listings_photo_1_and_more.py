# Generated by Django 5.0 on 2023-12-21 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='listing_date',
            field=models.DateField(default=datetime.datetime(2023, 12, 21, 11, 36, 11, 925220)),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_1',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925040'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_10',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925203'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_2',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925060'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_3',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925078'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_4',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925097'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_5',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925114'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_6',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925133'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_7',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925151'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_8',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925169'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_9',
            field=models.ImageField(blank=True, upload_to='photos/2023-12-21 11:36:11.925185'),
        ),
        migrations.AlterField(
            model_name='listings',
            name='photo_main',
            field=models.ImageField(upload_to='photos/2023-12-21 11:36:11.925013'),
        ),
    ]
