# Generated by Django 3.1.7 on 2021-03-18 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorCourses', '0018_auto_20210318_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='uploaded_at',
        ),
    ]