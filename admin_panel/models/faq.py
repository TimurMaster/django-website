from django.db import models

class FAQ(models.Model):
    question = models.TextField(default="")
    answer = models.TextField(default="")