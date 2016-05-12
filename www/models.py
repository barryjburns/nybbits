from django.db import models
from uuid import uuid4

# Create your models here.

default_page_content = '''{% extends 'www/base.html' %}

{% block head %}
{% endblock %}

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

def gen_ticket_id(): return str(uuid4().int())[3:8]

class Ticket(models.Model):
  name = models.CharField(max_length = 255, blank = False, null = False, unique = False)
  email = models.CharField(max_length = 255, blank = False, null = False, unique = False)
  phone = models.CharField(max_length = 255, blank = False, null = False, unique = False)
  subject = models.CharField(max_length = 255, blank = False, null = False, unique = False)
  body = models.TextField(blank = False, null = False, unique = False)
  number = models.CharField(max_length = 16, blank = False, null = False, unique = True, db_index = True, default = gen_ticket_id)
  created = models.DateTimeField(auto_now_add = True)
  modified = models.DateTimeField(auto_now = True)
  closed = models.DateTimeField(null = True, blank = True, default = None)

  def __str__(self):
    result = '[%s] %s: %s' % (self.number, self.name, self.created)
    if self.closed is not None: return '%s (closed)' % result
    else: return '%s (open)' % result
