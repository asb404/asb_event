# Generated by Django 3.0.5 on 2021-03-26 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antpage', '0010_remove_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='elike',
            field=models.CharField(default='f', max_length=1),
        ),
    ]