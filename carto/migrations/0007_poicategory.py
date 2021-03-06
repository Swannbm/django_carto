# Generated by Django 2.1.7 on 2019-03-13 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carto', '0006_delete_quotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='POICategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('color_id', models.CharField(choices=[('1', 'Blue'), ('2', 'Red'), ('3', 'Green'), ('4', 'Orange'), ('5', 'Yellow'), ('6', 'Violet'), ('7', 'Grey'), ('8', 'Black')], default='3', max_length=1)),
            ],
        ),
    ]
