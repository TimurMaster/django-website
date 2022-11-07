from django.db import models

# Create your models here.
class Tovar(models.Model):
    name = models.CharField(max_length=255, default="")
    description = models.TextField(default="")
    short_description = models.TextField(default="")
    search_info = models.TextField(default="")

class TovarChar(models.Model):
    tovar = models.ForeignKey(Tovar,
                              on_delete=models.CASCADE,
                              related_name="char",
                              )
    key = models.CharField(max_length=255,default="")
    value = models.TextField(default="")

class TovarImages(models.Model):
    tovar = models.ForeignKey(Tovar,
                              on_delete=models.CASCADE,
                              related_name="img",
                              )
    img = models.ImageField(upload_to='tovar_files/images', default='tovar_files/pictures/Bi-group.png')
    logo = models.ImageField(upload_to='tovar_files/images/logo', default='tovar_files/pictures/Bi-group.png')
