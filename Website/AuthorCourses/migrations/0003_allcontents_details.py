# Generated by Django 3.1.7 on 2021-03-17 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AuthorCourses', '0002_auto_20210316_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllContents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentName', models.CharField(max_length=200)),
                ('contentBody', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=500)),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AuthorCourses.allcontents')),
            ],
        ),
    ]