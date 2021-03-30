from django.db import models

from myapp.settings import BASE_URL


class ShortUrl(models.Model):
    original_path = models.TextField()
    slug = models.TextField(unique=True)

    @property
    def short_path(self):
        return f'su{self.slug}'

    @property
    def original_url(self):
        return BASE_URL + self.original_path

    @property
    def short_url(self):
        return BASE_URL + self.short_path
