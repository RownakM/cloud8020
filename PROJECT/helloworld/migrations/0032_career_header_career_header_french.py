# Generated by Django 3.2.11 on 2022-04-09 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0031_career_data_career_data_french_career_sub_data_career_sub_data_french'),
    ]

    operations = [
        migrations.CreateModel(
            name='career_header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200, verbose_name='Header Text')),
                ('sub', models.CharField(max_length=100, verbose_name='Sub text')),
            ],
        ),
        migrations.CreateModel(
            name='career_header_french',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=200, verbose_name='Header Text')),
                ('sub', models.CharField(max_length=100, verbose_name='Sub text')),
            ],
        ),
    ]
