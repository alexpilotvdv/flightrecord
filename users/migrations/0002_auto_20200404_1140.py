# Generated by Django 3.0.5 on 2020-04-04 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['lastname'], 'verbose_name': 'Член клуба', 'verbose_name_plural': 'Члены клуба'},
        ),
    ]