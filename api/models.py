import time

from django.db import models


class Url(models.Model):
    main_url = models.URLField()
    short_url = models.IntegerField()
    short_url_view = models.CharField(max_length=255)
    time_url = models.DateField(auto_now=True)
    lifetime = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.short_url
