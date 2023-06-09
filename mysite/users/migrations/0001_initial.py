# Generated by Django 4.1.7 on 2023-03-29 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_level', models.CharField(max_length=10)),
                ('user_id', models.CharField(max_length=15)),
                ('user_phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_name', models.CharField(max_length=20)),
                ('vehicle_id', models.CharField(max_length=15)),
                ('vehicle_age', models.CharField(max_length=3)),
                ('vehicle_addres', models.CharField(max_length=100)),
                ('vehicle_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.users')),
            ],
        ),
    ]
