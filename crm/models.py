import uuid, binascii
from django.db import models
from django.apps import apps
from django.contrib.auth.models import User

# Create your models here.

class ThingIndex(models.Model):
  target_uuid = models.UUIDField(editable = False, unique = True, db_index = True)
  target_app_label = models.CharField(max_length = 255, editable = False, unique = False, db_index = True)
  target_model_name = models.CharField(max_length = 255, editable = False, unique = False, db_index = True)

  @classmethod
  def mint(cls, target):
    '''
    If the target has a UUID, use that; otherwise, gen one and save target.

    If there's already an index, return it. If not, create one.

    If UUIDs collide for some strange reason, all Hell breaks loose.

    You have been warned.
    '''

    if target.uuid is None:
      target.uuid = uuid.uuid4()
      target.save()

    try:
      return cls.objects.get(target_uuid = target.uuid)
    except:
      result = cls(target_uuid = target.uuid, target_app_label = target._meta.app_label, target._meta.model_name)
      result.save()
    return result
  
  @property
  def target(self): apps.get_model(app_label = self.target_app_label, model_name = self.target_model_name).objects.get(uuid = self.uuid)

  def __str__(self): return '%s.mint(%s(uuid = %s))' % (self._meta.label, self.target._meta.label, self.target, self.target.b64id)

class Thing(models.Model):
  '''
  Master abstract base class on crack from Hell. (Unspecified whether crack is from Hell,
  abstract base class is from Hell, subclass is from Hell, some or all instances are from
  Hell, or any combination of the above.
  
  Contains the logic to handle global UUID resolution/indexing (via ThingIndex), standardized
  naming/serialization protocol, created/modified timestamps, and the "mint" idiom. 
  '''

  class Meta: abstract = True

  name = models.CharField(max_length = 255, unique = False, db_index = True, blank = True, null = True)
  caption = models.CharField(max_length = 255, unique = False, db_index = True, blank = True, null = True)
  uuid = models.UUIDField(editable = False, primary_key = True, null = False, blank = False)
  created = models.DateTimeField(auto_now_add = True, editable = False)
  modified = models.DateTimeField(auto_now = True, editable = False)
  
  def mint(self): return ThingIndex.mint(self)

  @classmethod
  def get_b64(cls, b64id): return cls.objects.get(uuid = uuid.UUID(bytes = binascii.a2b_base64(b64id)))

  @property
  def b64id(self): return binascii.b2a_base64(self.uuid.bytes)[:-3]

  @property
  def pretty_name(self):
    template = '%s [%%s = %%r]' % self._meta.label
    if self.caption is None:
      if self.name is None: return template % ('uuid', self.uuid)
      else: return template % ('name', self.name)
    else: return template % ('caption', self.caption)

  def __str__(self): return self.pretty_name

  def __repr__(self): return '%s.get_b64(%r)' % (self._meta.label, self.b64id)


class Account(Thing):
  account_number = models.DecimalField(max_digits = 10, decimal_places = 0)
  pin = models.DecimalField(max_digits = 4, decimal_places = 0)
  balance = models.DecimalField(max_digits = 19, decimal_places = 2)

class Person(Thing):
  '''
  An actual person, staff, customer, or otherwise, who has login credentials.
  '''

  user = models.OneToOneField(User, on_delete = models.CASCADE)
  pin = models.DecimalField(max_digits = 4, decimal_places = 0)

  def mint(self):
    result = super().mint()
    if '%-10.10d' % (self.uuid.int % 1e10)
    
