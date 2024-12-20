# Generated by Django 5.1 on 2024-10-28 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumnos',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Caballo',
            fields=[
                ('id_caballo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id_competencia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=255)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id_disciplina', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('dni', models.CharField(max_length=9, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=255)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Raza',
            fields=[
                ('id_raza', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('id_clase', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.categoria')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.profesor')),
            ],
        ),
        migrations.CreateModel(
            name='AlumnosXClase',
            fields=[
                ('id_alumnos_clase', models.AutoField(primary_key=True, serialize=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.alumnos')),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.clase')),
            ],
        ),
        migrations.CreateModel(
            name='AlumnosXCompetencia',
            fields=[
                ('id_alumnos_competencia', models.AutoField(primary_key=True, serialize=False)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.alumnos')),
                ('competencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.competencia')),
            ],
        ),
        migrations.CreateModel(
            name='Cuota',
            fields=[
                ('id_cuota', models.AutoField(primary_key=True, serialize=False)),
                ('mes', models.CharField(max_length=20)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fecha_pago', models.DateField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.alumnos')),
            ],
        ),
        migrations.CreateModel(
            name='CaballoXDisciplina',
            fields=[
                ('id_caballo_x_disciplina', models.AutoField(primary_key=True, serialize=False)),
                ('caballo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.caballo')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='Montura',
            fields=[
                ('id_montura', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.alumnos')),
                ('caballo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.caballo')),
            ],
        ),
        migrations.CreateModel(
            name='CaballoXRaza',
            fields=[
                ('id_caballo_x_raza', models.AutoField(primary_key=True, serialize=False)),
                ('caballo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.caballo')),
                ('raza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.raza')),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id_turno', models.AutoField(primary_key=True, serialize=False)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mi_app.categoria')),
            ],
        ),
    ]
