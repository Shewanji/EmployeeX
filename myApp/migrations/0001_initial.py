# Generated by Django 4.2.11 on 2024-03-20 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('hire_date', models.DateField()),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('department', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
        ),
    ]
