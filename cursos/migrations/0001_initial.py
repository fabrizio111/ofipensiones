# Generated by Django 3.2.6 on 2024-10-06 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grado', models.CharField(max_length=5)),
                ('grupo', models.CharField(max_length=5)),
                ('jornada', models.CharField(max_length=15)),
            ],
        ),
    ]
