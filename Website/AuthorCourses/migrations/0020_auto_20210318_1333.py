# Generated by Django 3.1.7 on 2021-03-18 08:03

import AuthorCourses.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorCourses', '0019_remove_document_uploaded_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[AuthorCourses.validators.validate_file]),
        ),
    ]
