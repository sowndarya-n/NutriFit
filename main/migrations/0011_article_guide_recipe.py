# Generated by Django 4.2.13 on 2024-11-02 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0010_fitnessequipment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="img/articles/"),
                ),
                ("link", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Guide",
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
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="img/guides/"),
                ),
                ("content", models.TextField()),
                ("yt_link", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Recipe",
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
                ("description", models.TextField()),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="img/recipes/"),
                ),
                ("detailed_instructions", models.TextField()),
                ("ingredients", models.TextField()),
                ("yt_link", models.URLField(blank=True, null=True)),
            ],
        ),
    ]
