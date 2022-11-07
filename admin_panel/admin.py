from django.contrib import admin

from .models import *

admin.site.register(Tovar)
admin.site.register(Category)
admin.site.register(TovarCategory)
admin.site.register(TovarChar)
admin.site.register(TovarImages)
admin.site.register(Client)
admin.site.register(Partner)
admin.site.register(Project)
admin.site.register(ProjectImages)
admin.site.register(CategoryTable)
admin.site.register(CategoryTableValue)
admin.site.register(HeaderContact)
admin.site.register(Address)
admin.site.register(Card)

# Register your models here.
