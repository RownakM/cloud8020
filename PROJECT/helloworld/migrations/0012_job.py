# Generated by Django 3.2.11 on 2022-02-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helloworld', '0011_remove_sub_solutions_service_subtext'),
    ]

    operations = [
        migrations.CreateModel(
            name='job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_Title', models.CharField(max_length=200)),
                ('Job_Type', models.CharField(choices=[('Full Time', 'Full Time'), ('Permanent', 'Permanent'), ('Part-Time', 'Part-Time'), ('Contract', 'Contract'), ('Temporary', 'Temporary'), ('Casual', 'Casual'), ('Apprenticeship', 'Apprenticeship'), ('Internship', 'Internship'), ('Freelance', 'Freelance')], max_length=200)),
                ('Job_Category', models.CharField(choices=[('Job category', 'Job Category')], max_length=300)),
                ('Country', models.CharField(choices=[], max_length=300)),
                ('State', models.CharField(choices=[], max_length=300)),
            ],
        ),
    ]
