# Generated by Django 4.2.11 on 2024-03-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("noticias", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="noticias",
            name="data",
            field=models.DateField(help_text="aaaa-mm-dd"),
        ),
    ]
