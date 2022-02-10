# Generated by Django 3.1.13 on 2021-09-23 00:06

from django.db import migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('rolodex', '0020_auto_20210922_2337'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default='America/Los_Angeles', help_text='Timezone of the project / working hours', verbose_name='Project Timezone'),
        ),
    ]