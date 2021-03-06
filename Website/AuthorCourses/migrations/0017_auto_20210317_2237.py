# Generated by Django 3.1.7 on 2021-03-17 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorCourses', '0016_remove_allcontents_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='allcontents',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AuthorCourses.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='allcontents',
            name='doc',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AuthorCourses.document'),
            preserve_default=False,
        ),
    ]
