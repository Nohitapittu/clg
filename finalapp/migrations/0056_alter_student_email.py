# Generated by Django 4.2.7 on 2023-12-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalapp', '0055_alter_teacher_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
