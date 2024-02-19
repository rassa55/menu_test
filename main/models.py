from django.db import models
from django.urls import reverse

class Menu(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'main_menu'

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    named_url = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'main_menuitem'