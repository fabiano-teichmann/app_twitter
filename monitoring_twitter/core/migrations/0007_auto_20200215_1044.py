# Generated by Django 3.0.3 on 2020-02-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200215_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
