# Generated by Django 4.1.7 on 2023-04-19 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_basicdata_doctor_healthydata_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='aaa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=15)),
                ('e_mail', models.EmailField(max_length=254)),
            ],
        ),
    ]
