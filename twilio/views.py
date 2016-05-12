from django.shortcuts import render

from django.http import HttpResponse, HttpResponseNotFound

from django.template import Template, Context
from xml.dom import minidom
from django.views.decorators.csrf import csrf_exempt
import traceback, re

from .models import TwilioMessage

def parse_incoming(request):
  TwilioMessage(
    to_country = request.POST['ToCountry'],
    to_state = request.POST['ToState'],
    sms_message_sid = request.POST['SmsMessageSid'],
    num_media = request.POST['NumMedia'],
    to_city = request.POST['ToCity'],
    from_zip = request.POST['FromZip'],
    sms_sid = request.POST['SmsSid'],
    from_state = request.POST['FromState'],
    sms_status = request.POST['SmsStatus'],
    from_city = request.POST['FromCity'],
    body = request.POST['Body'],
    to_e164  = request.POST['To'],
    messaging_service_sid  = request.POST['MessagingServiceSid'],
    to_zip  = request.POST['ToZip'],
    num_segments  = request.POST['NumSegments'],
    message_sid  = request.POST['MessageSid'],
    account_sid  = request.POST['AccountSid'],
    from_e164  = request.POST['From'],
    api_version  = request.POST['ApiVersion']
  ).save()

  response = 'Thank you for contacting Nybbits! :-) You will receive a call back shortly from the on-call technician.'
  return HttpResponse(response, content_type = 'text/plain')

@csrf_exempt
def inbound(request):
  try: return parse_incoming(request)
  except: return HttpResponse(traceback.format_exc(), content_type = 'text/plain')
