from django.contrib import admin

# Register your models here.
from .models import AllContents, Category, Document

admin.site.register(Category)
admin.site.register(AllContents)
admin.site.register(Document)