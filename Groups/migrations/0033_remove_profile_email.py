# Generated by Django 3.1.1 on 2020-10-04 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0032_auto_20201004_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]