# Generated by Django 3.0.3 on 2020-02-16 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20200216_0850'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='RequestAPI',
        ),
    ]