# Generated by Django 3.0.5 on 2021-03-26 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antpage', '0008_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(default='f', max_length=10),
        ),
    ]