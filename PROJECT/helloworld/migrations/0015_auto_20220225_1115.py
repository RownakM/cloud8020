# Generated by Django 3.2.11 on 2022-02-25 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0014_auto_20220225_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='Country',
            field=models.CharField(choices=[('India', 'India')], max_length=300),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='State',
            field=models.CharField(choices=[('Wb', 'Wb')], max_length=300),
        ),
    ]
