from django.contrib import admin

# Register your models here.

from .models import Page, Sidebar

for model in Page, Sidebar: admin.site.register(model)
