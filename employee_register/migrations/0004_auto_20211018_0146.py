# Generated by Django 3.2.8 on 2021-10-17 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0003_auto_20211016_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='image_url',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Address',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Email',
            field=models.EmailField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_code',
            field=models.CharField(max_length=5),
        ),
    ]