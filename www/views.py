from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.template import Template, Context

from .models import Page, Sidebar, Ticket
from django.template import RequestContext

# Create your views here.

def contact_submit(request):
  try:
    ticket = Ticket(
      name = request.POST['name'],
      email = request.POST['email'],
      subject = request.POST['subject'],
      body = request.POST['body']
    )
    ticket.save()
    return HttpResponseRedirect('/contact-success')
  except:
    return HttpResponseRedirect('/contact-fail')

     

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
  context = RequestContext(request)
  context.update(namespace)
  return response_class(template.render(context))
