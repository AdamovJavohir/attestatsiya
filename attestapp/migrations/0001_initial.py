# Generated by Django 4.2.18 on 2025-02-01 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AttastModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('familiya', models.CharField(max_length=50)),
                ('tell', models.PositiveIntegerField()),
                ('ruyxatdanUtishVaqti', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
