# Generated by Django 3.2.6 on 2024-10-08 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0002_auto_20241007_2133'),
        ('cronogramasAlumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cronogramaalumno',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cronogramaalumno',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='cronogramaalumno',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alumnos.alumno'),
        ),
        migrations.AlterField(
            model_name='cronogramaalumno',
            name='concepto',
            field=models.CharField(choices=[('matricula', 'Matricula'), ('pension', 'Pension'), ('otros', 'Otro Pago')], max_length=20),
        ),
        migrations.AlterField(
            model_name='cronogramaalumno',
            name='mes',
            field=models.CharField(max_length=20),
        ),
    ]