# Generated by Django 4.2.13 on 2024-11-06 04:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0012_essentials_membershiprequest_user_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="detailed_info",
            field=models.TextField(default="NA"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img/"),
        ),
        migrations.AlterField(
            model_name="essentials",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="img/"),
        ),
    ]
