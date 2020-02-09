# Generated by Django 3.0.3 on 2020-02-09 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_publish', models.DateTimeField()),
                ('author', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=280)),
            ],
        ),
    ]