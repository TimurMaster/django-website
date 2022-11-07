from django.db import models

class Client(models.Model):
    img = models.ImageField(upload_to='Client_files/images', default='tovar_files/pictures/Bi-group.png')

