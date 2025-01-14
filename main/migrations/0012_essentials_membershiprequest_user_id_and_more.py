# Generated by Django 4.2.13 on 2024-11-06 03:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0011_article_guide_recipe"),
    ]

    operations = [
        migrations.CreateModel(
            name="Essentials",
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
                ("yt_link", models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="MembershipRequest",
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
                ("email", models.EmailField(max_length=254)),
                ("plan", models.CharField(max_length=100)),
                ("subscription_type", models.CharField(max_length=10)),
                ("submitted_at", models.DateTimeField(auto_now_add=True)),
                ("approved_status", models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="id",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="UserSubscription",
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
                ("plan", models.CharField(max_length=50)),
                (
                    "subscription_type",
                    models.CharField(
                        choices=[("Monthly", "Monthly"), ("Yearly", "Yearly")],
                        max_length=10,
                    ),
                ),
                ("start_date", models.DateField()),
                ("expiry_date", models.DateField()),
                ("email", models.EmailField(max_length=254, unique=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
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
                ("phone", models.CharField(blank=True, max_length=15, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
