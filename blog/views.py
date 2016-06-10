from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from www.models import Page, Sidebar
from .models import Entry, Tag, EntryTag
import datetime

def blog_entry(request, slug):
  entry = get_object_or_404(Entry, slug = slug)
  ctx = RequestContext(request)
  ctx.update({
    'entry': entry,
    'sidebar': Sidebar.objects.order_by('position'),
    'site_caption': 'Nybbits',
    'page_url': '/blog/' + entry.slug,
    'page_caption': entry.caption,
  })
  return render(request, 'blog/entry.html', ctx)

def blog_entries(request):
  entries = Entry.objects.all().filter(published__lte = datetime.datetime.utcnow()).exclude(deleted__lte = datetime.datetime.utcnow()).order_by('-published')[:10]
  ctx = RequestContext(request)
  ctx.update({
    'latest': entries[0],
    'entries': entries,
    'sidebar': Sidebar.objects.order_by('position'),
    'site_caption': 'Nybbits',
    'page_url': '/blog/',
    'page_caption': 'Blog',
  })
  return render(request, 'blog/entries.html', ctx)
