from django.contrib.auth.backends import BaseBackend
from .models import Client, VisaAdvisor

class ClientAuthenticationBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            client = Client.objects.get(username=username)
            if client.password == password:  # Compare plain text passwords
                return client
        except Client.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return Client.objects.get(pk=user_id)
        except Client.DoesNotExist:
            return None

class VisaAdvisorBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            advisor = VisaAdvisor.objects.get(username=username)
            if advisor.password == password:  # Compare plain text passwords
                return advisor
        except VisaAdvisor.DoesNotExist:
            pass
        return None

    def get_user(self, user_id):
        try:
            return VisaAdvisor.objects.get(pk=user_id)
        except VisaAdvisor.DoesNotExist:
            return None