# Generated by Django 3.2.11 on 2022-04-15 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0033_auto_20220415_0611'),
    ]

    operations = [
        migrations.AddField(
            model_name='career_sub_data',
            name='Fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='career_sub_data_french',
            name='Fee',
            field=models.IntegerField(default=0),
        ),
    ]
