# Generated by Django 3.0.5 on 2020-04-09 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_user_user_reg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_reg',
        ),
    ]
