# Generated by Django 4.0.6 on 2022-08-04 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='total_enrollment',
            field=models.IntegerField(default=0),
        ),
    ]
