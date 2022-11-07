from django.db import models

class HeaderContact(models.Model):
    worktime = models.TextField(default="")
    adress = models.TextField(default="")
    city = models.TextField(default="")
    phone = models.TextField(default="")
    email = models.TextField(default="")
    holidaytime = models.TextField(default="")
