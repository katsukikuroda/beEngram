# Generated by Django 4.0rc1 on 2022-01-19 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_user_email_alter_user_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
