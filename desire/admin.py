from django.contrib import admin
from desire.models import Client
from desire.models import VisaAdvisor
from desire.models import customerquerry
from desire.models import ClientDocument
from desire.models import Contact
from desire.models import Adviserquerry

admin.site.register(Client)
admin.site.register(VisaAdvisor)
admin.site.register(customerquerry)
admin.site.register(ClientDocument)
admin.site.register(Contact)
admin.site.register(Adviserquerry)
