# Generated by Django 3.2.11 on 2022-03-18 04:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0027_corpo_data_corpo_data_french_corpo_header_corpo_header_french'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_info',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]