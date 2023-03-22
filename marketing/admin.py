from django.contrib import admin
from . models import MailMessage, Subscribers


admin.site.register(MailMessage)
admin.site.register(Subscribers)
