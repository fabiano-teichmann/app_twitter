# Generated by Django 3.0.3 on 2020-02-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_hashtag'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='hashtag',
            field=models.CharField(default=None, max_length=60),
            preserve_default=False,
        ),
    ]
