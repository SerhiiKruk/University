# Generated by Django 3.1.1 on 2020-09-21 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0015_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
