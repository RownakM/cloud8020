# Generated by Django 3.2.11 on 2022-02-21 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0005_aboutus_french_brand_text_french_contactmodel_address_french_contactmodel_email_french_contactmodel_'),
        ('About', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_french',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage About Us(French)',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.aboutus',),
        ),
    ]