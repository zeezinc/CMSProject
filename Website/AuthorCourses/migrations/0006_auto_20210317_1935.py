# Generated by Django 3.1.7 on 2021-03-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorCourses', '0005_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='allcontents',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AuthorCourses.category'),
            preserve_default=False,
        ),
    ]
