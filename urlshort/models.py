from django.db import models

# Create your models here.
class ShortURL(models.Model):
    original_url = models.URLField(max_length = 1000)
    short_url = models.CharField(max_length = 100)
    date_time_created = models.DateTimeField()

    def __str__(self) -> str:
        return self.original_url
    