from django.db import models

# Create your models here.

default_page_content = '''{% extends 'www/base.html' %}

{% block content %}
  Add some content.
{% endblock %}
'''

class Page(models.Model):
  name = models.CharField(max_length = 64, blank = False, null = False, unique = True, db_index = True)
  caption = models.CharField(max_length = 255, blank = False, null = False, unique = False)
  position = models.IntegerField(null = True, blank = True, default = None)
  content = models.TextField(null = False, blank = True, default = default_page_content)

  def __str__(self): return '%s ("%s")' % (self.name, self.caption)

class Sidebar(models.Model):
  caption = models.CharField(max_length = 255, blank = False, null = False, unique = False)
  position = models.IntegerField(null = False, default = 0)
  url = models.CharField(max_length = 255, null = False)

  def __str__(self): return '%s -> %s' % (self.caption, self.url)
