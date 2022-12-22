from django.db import models
from django.utils.text import slugify
import uuid
from django.db.models.signals import pre_save

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, )
    date_updated = models.DateTimeField(auto_now=True,)


def pre_save_note_receiver(sender, instance, **kwargs):
    instance.slug = slugify(instance.title)


pre_save.connect(pre_save_note_receiver, sender=Note)
