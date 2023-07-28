from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.text import slugify
from django.utils.html import mark_safe


# Create your models here.
class Category(MPTTModel, models.Model):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="images/", null=True)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/" % (self.slug)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    @property
    def photo_preview(self):
        if self.photo:
            return mark_safe(
                '<img src="{}" width="150" height="150" />'.format(self.photo.url)
            )
        return ""


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", on_delete=models.PROTECT, null=True, blank=True
    )

    def __str__(self):
        return self.name
