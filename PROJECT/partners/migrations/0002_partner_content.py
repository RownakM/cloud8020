# Generated by Django 3.2.11 on 2022-02-20 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0002_sub_partners'),
        ('partners', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner_Content',
            fields=[
            ],
            options={
                'verbose_name_plural': 'Manage Partner Content',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('helloworld.sub_partners',),
        ),
    ]
