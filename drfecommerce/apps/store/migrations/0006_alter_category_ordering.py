# Generated by Django 4.1.7 on 2023-07-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0005_alter_category_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="ordering",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
