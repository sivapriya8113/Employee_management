# Generated by Django 3.2.8 on 2021-10-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0004_auto_20211018_0146'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='image_url',
        ),
        migrations.AddField(
            model_name='employee',
            name='EMPimage',
            field=models.ImageField(default='', upload_to=None),
        ),
    ]
