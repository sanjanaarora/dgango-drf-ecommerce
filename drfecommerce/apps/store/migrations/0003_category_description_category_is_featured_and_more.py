# Generated by Django 4.1.7 on 2023-07-28 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_remove_product_category_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="is_featured",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="ordering",
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name="category",
            name="photo",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(editable=False, null=True),
        ),
    ]
