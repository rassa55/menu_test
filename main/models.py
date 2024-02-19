from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            return reverse(self.named_url)
        return '#'