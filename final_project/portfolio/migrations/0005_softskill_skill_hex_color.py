# Generated by Django 5.0.6 on 2024-06-09 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_softskill'),
    ]

    operations = [
        migrations.AddField(
            model_name='softskill',
            name='skill_hex_color',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
