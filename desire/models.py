from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    username=models.CharField(max_length=50)
    address=models.TextField(null=True)
    dob=models.DateField(blank=True,null=True)
    email=models.TextField(null=True)
    phoneno=models.IntegerField(null=True)
    password=models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True) 
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
   
    @property
    def is_authenticated(self):
        # Always return True as this is a simple way to tell if the user is authenticated
        return True

    def has_perm(self, perm, obj=None):
        # Simplest implementation: return True if user is an admin, else False
        return self.is_superuser

    def has_module_perms(self, app_label):
        # Simplest implementation: return True if user is an admin, else False
        return self.is_superuser

    def get_username(self):
        """Return the identifying username for this User, which is the email in this case."""
        return self.email

    def __str__(self):
        return self.email
    
class VisaAdvisor(models.Model):
    username=models.CharField(max_length=50)
    email=models.TextField(null=True)
    phoneno=models.IntegerField(null=True)
    password=models.TextField(null=True)
    experience=models.TextField(null=True)
    country_specialization=models.TextField(null=True)
    education=models.TextField(null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True) 
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
   
    @property
    def is_authenticated(self):
        # Always return True as this is a simple way to tell if the user is authenticated
        return True

    def has_perm(self, perm, obj=None):
        # Simplest implementation: return True if user is an admin, else False
        return self.is_superuser

    def has_module_perms(self, app_label):
        # Simplest implementation: return True if user is an admin, else False
        return self.is_superuser

    def get_username(self):
        """Return the identifying username for this User, which is the email in this case."""
        return self.email

    def __str__(self):
        return self.email
    
class customerquerry(models.Model):
    email=models.TextField()
    query=models.TextField()
    adviser=models.ForeignKey(to="VisaAdvisor",on_delete=models.CASCADE,default=True)
    
    def __str__(self) -> str:
        return self.email
    
    
class Adviserquerry(models.Model):
    email=models.TextField()
    query=models.TextField()
   
    def __str__(self) -> str:
        return self.email
    
class ClientDocument(models.Model):
    email=models.TextField(default=True)
    aadharcard=models.ImageField(upload_to='clientimg')
    paancard=models.ImageField(upload_to='clientimg')
    passport=models.ImageField(upload_to='clientimg')
    adviser=models.ForeignKey(to="VisaAdvisor",on_delete=models.CASCADE,default=True)
    
    def __str__(self) -> str:
        return self.email
    
class Contact(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phonenumber=models.IntegerField()
    message=models.TextField(max_length=200)
    
    def __str__(self) -> str:
        return self.first_name
   
    
    
