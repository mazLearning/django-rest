from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os, random


# Create your models here.

def get_filename(filename):
    basename = os.path.basename(filename)
    name, ext = os.path.splitext(basename)
    return name, ext


def upload_image_file(instance, filename):
    name, ext = get_filename(filename)
    random_name_number = random.randint(0, 100000000)
    new_filename = f"{instance.pk}--{random_name_number}{ext}"
    return f"image_article/{new_filename}"


class ArticleManager(models.Manager):
    def get_article_publish(self):
        return self.get_queryset().filter(status=True)

    def get_article_by_slug(self, slug):
        return self.get_queryset().filter(status=True, slug__iexact=slug).distinct()


class Article(models.Model):
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_file, null=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    objects = ArticleManager()

    def __str__(self):
        return self.title
