# Generated by Django 3.2.11 on 2022-02-21 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0005_aboutus_french_brand_text_french_contactmodel_address_french_contactmodel_email_french_contactmodel_'),
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solutions_french',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Create / Manage Solutions (French)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.solutions_french',),
        ),
        migrations.CreateModel(
            name='SubSolutions_french',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Create / Manage Sub Solutions (French)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.sub_solutions_french',),
        ),
    ]
