# Generated by Django 5.0.6 on 2024-06-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_name', models.CharField(max_length=50)),
                ('header_subtitle', models.CharField(max_length=50)),
                ('header_attr', models.CharField(max_length=50)),
            ],
        ),
    ]
