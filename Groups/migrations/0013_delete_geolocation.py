# Generated by Django 3.1.1 on 2020-09-20 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0012_auto_20200920_1239'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeoLocation',
        ),
    ]