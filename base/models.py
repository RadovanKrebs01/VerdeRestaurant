from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class Picture(models.Model):
    image = models.ImageField(storage=fs, null=True, blank=True)
