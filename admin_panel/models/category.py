from django.db import models
from .tovar import Tovar


class Category(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL,
                               related_name="childs",
                               )
    name = models.CharField(max_length=255)
    description = models.TextField(default="")
    img = models.ImageField(upload_to='category_files/images', default='tovar_files/pictures/Bi-group.png')

    def __str__(self):
        if self.parent:
            return str(self.parent) + '-' + self.name
        else:
            return self.name

class TovarCategory(models.Model):
    tovar = models.ForeignKey(Tovar,
                                on_delete=models.CASCADE,
                                related_name="categories",
                                )
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="companies",
                                 )

class CategoryTable(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name="table"
                                 )
    key = models.CharField(max_length=255)

class CategoryTableValue(models.Model):
    table = models.ForeignKey(CategoryTable,
                              on_delete=models.CASCADE,
                              related_name="values"
                              )
    value = models.TextField(default="")
