# Generated by Django 4.2.11 on 2024-03-22 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0002_address_department_role_leaverequest_document_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employee',
            name='role',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
