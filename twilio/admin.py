from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.

from .models import Pair, Message, EndPoint, TwilioMessage

for model in Pair, Message, EndPoint, TwilioMessage: admin.site.register(model)

