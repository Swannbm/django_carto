# Generated by Django 2.1.7 on 2019-03-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carto', '0003_pointofinterest_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pointofinterest',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
