# Generated by Django 2.1.7 on 2019-03-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carto', '0002_auto_20190307_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='pointofinterest',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
