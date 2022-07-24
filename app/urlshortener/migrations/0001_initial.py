# Generated by Django 3.1.4 on 2022-07-24 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlShortener',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originUrl', models.CharField(max_length=250, unique=True)),
                ('shortUrl', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('visit', models.IntegerField(default=0)),
            ],
        ),
    ]
