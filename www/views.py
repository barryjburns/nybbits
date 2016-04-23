from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.template import Template, Context

from .models import Page, Sidebar

# Create your views here.

def render_page(request, name):
  namespace = {}
  namespace['page_url'] = '/' + name
  namespace['pages'] = Page.objects.filter(position__isnull = False).order_by('position')
  namespace['site_caption'] = 'Nybbits'
  namespace['sidebar'] = Sidebar.objects.order_by('position')
  namespace['request'] = request

  response_class = HttpResponse

  try:
    page = Page.objects.get(name = name)
  except:
    page = Page.objects.get(name = '404')
    response_class = HttpResponseNotFound

  namespace['page_caption'] = page.caption
  namespace['page_name'] = name

  template = Template(page.content)
  context = Context(namespace)
  return response_class(template.render(context))
