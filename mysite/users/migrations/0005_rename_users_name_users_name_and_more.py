# Generated by Django 4.1.7 on 2023-03-29 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_users_level_users_level_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='users_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='vehicle',
            old_name='vehicle_name',
            new_name='name',
        ),
    ]
