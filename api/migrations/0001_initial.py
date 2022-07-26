# Generated by Django 4.0.6 on 2022-07-26 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_url', models.URLField()),
                ('short_url', models.IntegerField()),
                ('short_url_view', models.CharField(max_length=255)),
                ('time_url', models.DateField(auto_now=True)),
                ('lifetime', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
