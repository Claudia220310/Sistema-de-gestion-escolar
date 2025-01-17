# Generated by Django 5.0.6 on 2024-06-21 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0008_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('no_documento', models.CharField(max_length=20)),
                ('grado', models.CharField(max_length=50)),
                ('genero', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino'), ('N', 'No aplica')], max_length=1)),
                ('direccion', models.CharField(max_length=255)),
                ('padre_familia', models.CharField(max_length=100)),
                ('numero_padre', models.CharField(max_length=15)),
            ],
        ),
    ]
