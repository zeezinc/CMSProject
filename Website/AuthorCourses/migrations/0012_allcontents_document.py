# Generated by Django 3.1.7 on 2021-03-17 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorCourses', '0011_remove_allcontents_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcontents',
            name='document',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='AuthorCourses.document'),
            preserve_default=False,
        ),
    ]
