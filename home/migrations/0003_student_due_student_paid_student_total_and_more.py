# Generated by Django 4.1.3 on 2022-12-20 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_teacher_alter_student_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='due',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='paid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='student',
            name='total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='course',
            name='textfield',
            field=models.CharField(max_length=100),
        ),
    ]
