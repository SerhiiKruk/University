# Generated by Django 3.1.1 on 2020-10-03 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0024_student_avg_mark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='avg_mark',
            field=models.FloatField(default=0),
        ),
    ]