# Generated by Django 3.0.5 on 2021-03-26 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antpage', '0006_auto_20210326_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
