# Generated by Django 3.1.1 on 2020-09-20 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0011_auto_20200920_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='faculty',
            field=models.TextField(choices=[('Computer science and cybernetics', 'Kubik'), ('Information technology', 'Fit')]),
        ),
    ]