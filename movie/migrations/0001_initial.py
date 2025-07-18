# Generated by Django 5.2.4 on 2025-07-15 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("release_date", models.DateField()),
                ("duration", models.PositiveIntegerField()),
                ("synopsis", models.TextField()),
            ],
        ),
    ]
