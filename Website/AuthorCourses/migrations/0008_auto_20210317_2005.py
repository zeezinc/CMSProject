# Generated by Django 3.1.7 on 2021-03-17 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorCourses', '0007_auto_20210317_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='allcontents',
        ),
        migrations.AddField(
            model_name='allcontents',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AuthorCourses.category'),
            preserve_default=False,
        ),
    ]
