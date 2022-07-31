# Generated by Django 4.0.6 on 2022-07-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userorm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='Joe', max_length=30)),
                ('last_name', models.CharField(default='Chris', max_length=30)),
                ('username', models.CharField(default='trap45', max_length=30, null=True)),
                ('dob', models.DateField(null=True)),
            ],
        ),
    ]
