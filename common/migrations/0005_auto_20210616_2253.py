# Generated by Django 3.1.3 on 2021-06-16 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_remove_comment2_forest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment2',
            name='author',
        ),
        migrations.DeleteModel(
            name='Forest',
        ),
        migrations.DeleteModel(
            name='Comment2',
        ),
    ]
