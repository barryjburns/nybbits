
# See: https://www.twilio.com/docs/api/twiml/twilio_request
'''

SID: MG4c2e8d9c8d1643a1c8dd4c05b5aff2f2
Request URL: 		http://www.nybbits.com/twilio/inbound
Fallback URL :		http://www.nybbits.com/twilio/fallback
Status Callback URL:	http://www.nybbits.com/twilio/callback
Account Sid:  AC15e1388e19874911a94f0306eda12fcd
775dfd593a325e71f82c7d3824f63bca
API key: SKb20beae04271fa19f790bd47cfab3229
Secret: iapC4RY1odnBjIDrezXFcQ3KflwRfm6m
'''

from django.db import models
from uuid import uuid4
import re

_uuid = lambda: models.UUIDField(primary_key = True, editable = False, db_index = True, unique = True, default = uuid4)
_name = lambda: models.CharField(max_length = 255, unique = True, db_index = True)
_created = lambda: models.DateTimeField(auto_now_add = True, editable = False, db_index = True, blank = False, null = False)
_modified = lambda: models.DateTimeField(auto_now = True, editable = False, db_index = True, blank = False, null = False)
_future_event = lambda: models.DateTimeField(default = None, blank = True, null = True)
_string = lambda: models.TextField(default = '', null = False, blank = True)
_int = lambda: models.IntegerField(default = None, null = True)
e164_re = re.compile(r'\+1([2-9]\d\d)([2-9]\d\d)(\d{4})')

def fmt_e164(n):
  m = e164_re.match(n)
  if m is None: return n
  else: return '(%s) %s-%s' % m.groups()

class Pair(models.Model):
  name = _name()
  value = _string()

  def __str__(self): return '%s = %r' % (self.name, self.value)

  @classmethod
  def get_value(cls, name): return cls.objects.get(name = name).value

  @classmethod
  def set_value(cls, name, value):
    o = cls.objects.get(name = name)
    o.value = value
    o.save()

class Message(models.Model):
  uuid = _uuid()
  created = _created()
  modified = _modified()
  deleted = _future_event()
  queued = _future_event()
  processed = _future_event()

  to_ep = models.ForeignKey('EndPoint', related_name = 'send_message_set')
  from_ep = models.ForeignKey('EndPoint', related_name = 'received_message_set')
  content = models.TextField(blank = True, null = False, default = '')
  media_url = models.CharField(blank = True, null = True, default = None, max_length = 255)

class TwilioMessage(models.Model):
  uuid = _uuid()
  created = _created()
  deleted = _future_event()
  processed = _future_event()
  to_country = _string()
  to_state = _string()
  sms_message_sid = _string()
  num_media = _int()
  to_city = _string()
  from_zip = _string()
  sms_sid = _string()
  from_state = _string()
  sms_status = _string()
  from_city = _string()
  from_country = _string
  to_e164 = _string()
  messaging_service_sid = _string()
  to_zip = _string()
  num_segments = _int()
  message_sid = _string()
  account_sid = _string()
  from_e164 = _string()
  body = _string()
  api_version = models.DateField(default = None, null = True)

  def __str__(self): return '%s -> %s @ %s: %s' % (fmt_e164(self.from_e164), fmt_e164(self.to_e164), self.created, self.body[:160])

class EndPoint(models.Model):
  modified = _modified()
  created = _created()
  deleted = _future_event()
  is_internal = models.BooleanField(default = False, null = False)
  e164 = _name()
  opt_in = _future_event()

  def __str__(self):
    m = e164_re.match(self.e164)
    if m is None: result = self.e164
    else: result = '(%s) %s-%s' % m.groups()
    if self.is_internal: return '[local] ' + result
    else: return '[remote] ' + result

'''

class Promotion(models.Model):
  uuid = _uuid()
  created = _created()
  modified = _modified()  
  deleted = _future_event()
  content = models.TextField(blank = True, null = True

class PromotionBatch(models.Models):
  uuid = _uuid()
  created = _created()
  from_end_point = models.ForeignKey('EndPoint', related_name = 'promotion_batch_set_sent')
  to_end_point = models.ForeignKey('EndPoint', related_name = 'promotion_batch_set_received')
  promotion = models.ForeignKey('Promotion', 

'''
