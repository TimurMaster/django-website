from django.db import models

class Partner(models.Model):
    img = models.ImageField(upload_to='Partner_files/images', default='tovar_files/pictures/Bi-group.png')

