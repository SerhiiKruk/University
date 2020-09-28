# Generated by Django 3.1.1 on 2020-09-22 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0016_auto_20200921_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mark',
            name='semester',
            field=models.IntegerField(choices=[(1, 'First'), (2, 'Second')]),
        ),
        migrations.AlterField(
            model_name='mark',
            name='type',
            field=models.CharField(choices=[('Session', 'Exam'), ('Test', 'Test')], max_length=10),
        ),
    ]
