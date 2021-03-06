# Generated by Django 3.1.1 on 2020-09-21 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Groups', '0014_mark_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(verbose_name=[('Lecture', 'Lecture'), ('Practice', 'Practice')])),
                ('teacher', models.TextField(max_length=100)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Groups.subject')),
            ],
        ),
    ]
