# Generated by Django 3.0.5 on 2021-03-26 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antpage', '0004_auto_20210326_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(null=True, upload_to='image/'),
        ),
    ]
