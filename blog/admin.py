from django.contrib import admin
from blog.models import Category,Photo,Contact
# Register your models here.
admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Contact)