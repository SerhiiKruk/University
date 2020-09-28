# Generated by Django 3.1.1 on 2020-09-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0010_geolocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='course',
            field=models.IntegerField(choices=[(1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')], default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(default='2020-01-01'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='latitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='longitude',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
