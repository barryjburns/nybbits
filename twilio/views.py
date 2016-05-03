from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound

from django.template import Template, Context
from xml.dom import minidom
from django.views.decorators.csrf import csrf_exempt
import traceback, re

from .models import TwilioMessage

SMS_HELP_MESSAGE = '''Reply CALL to get a call back, JOIN to opt in to offers and information, STOP to opt out'''

def parse_incoming(request):
  message = TwilioMessage()
  fields = [
    ('ToCountry', 'to_country'),
    ('ToState', 'to_state'),
    ('SmsMessageSid', 'sms_message_sid'),
    ('NumMedia', 'num_media'),
    ('ToCity', 'to_city'),
    ('FromZip', 'from_zip'),
    ('SmsSid', 'sms_sid'),
    ('FromState', 'from_state'),
    ('SmsStatus', 'sms_status'),
    ('FromCity', 'from_city'),
    ('Body', 'body'),
    ('FromCountry', 'from_country'),
    ('To', 'to_e164'),
    ('MessagingServiceSid', 'messaging_service_sid'),
    ('ToZip', 'to_zip'),
    ('NumSegments', 'num_segments'),
    ('MessageSid', 'message_sid'),
    ('AccountSid', 'account_sid'),
    ('From', 'from_e164'),
    ('ApiVersion', 'api_version'),
  ]

  for post_var, model_field in fields:
    if post_var in request:
      setattr(message, model_field, request['post_var'])

  message.save()

  return HttpResponse('Thank you! :-) You will receive a call back shortly.', content_type = 'text/plain')

@csrf_exempt
def inbound(request):
  return parse_incoming(request)


"""

  try:
    return parse(request)
  except:
    return HttpResponse(traceback.format_exc(), content_type = 'text/plain')
"""
