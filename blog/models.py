from django.db import models
from django.utils.text import slugify
import markdown

class Entry(models.Model):
  class Meta:
    ordering = ['created']
    verbose_name_plural = 'entries'    
    get_latest_by = 'created'
    permissions = (('can_blog', 'Can write blog entries'),)

  caption = models.CharField(max_length = 255, blank = False, null = False)
  slug = models.SlugField(max_length = 255, unique = True, null = False, blank = False)
  created = models.DateTimeField(null = False, blank = False, auto_now_add = True)
  modified = models.DateTimeField(null = False, blank = False, auto_now = True)
  published = models.DateTimeField(null = True, blank = True, default = None)
  deleted = models.DateTimeField(null = True, blank = True, default = None)
  # Content is in Markdown format.
  mdcontent = models.TextField(null = False, blank = False)
  author = models.ForeignKey('auth.User', blank = False, null = False)
  
  def save(self, *args, **kwargs):
    if not self.slug: self.slug = slugify(self.caption)
    super(Entry, self).save(*args, **kwargs)

  @property
  def content(self): return markdown.markdown(self.mdcontent)

  def __str__(self):
    if self.published:
      return '%s (published by %s at %s)' % (self.caption, self.author.get_full_name(), self.published)
    else:
      return '%s (draft; created by %s at %s)' % (self.caption, self.author.get_full_name(), self.created)

class Tag(models.Model):
  slug = models.SlugField(max_length = 255, unique = True, null = False, blank = False)
  entry_set = models.ManyToManyField('Entry', through = 'EntryTag')

class EntryTag(models.Model):
  class Meta:
    unique_together = (('entry', 'tag'),)
    index_together = [
      ['entry', 'tag'],
    ]

  entry = models.ForeignKey('Entry', on_delete = models.CASCADE, null = False, blank = False, db_index = True)
  tag = models.ForeignKey('Tag', on_delete = models.CASCADE, null = False, blank = False, db_index = True)
