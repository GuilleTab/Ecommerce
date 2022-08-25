# Generated by Django 4.0.6 on 2022-08-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('puesto', models.CharField(max_length=100, null=b'I01\n')),
                ('fecha_nacimiento', models.DateField(blank=b'I01\n', null=b'I01\n')),
                ('año_ingreso', models.IntegerField()),
            ],
        ),
    ]
