from django.contrib import admin

from .models import Entry, Tag, EntryTag

for model in Entry, Tag, EntryTag: admin.site.register(model)
