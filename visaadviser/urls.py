"""visaadviser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from desire.views import (index,about,contact,service,country,login_client,registration
                          ,adviser,client,visaadvisor,clientadmin,paymentinfo,sendquery,profile,
                          senddocument,adindex,adclient_profile,ad_sendsuggest,adview_doc,
                          adview_recpay,adview_sugg,clientlogout,login_adviser,adviserproedit,
                          adviserlogout,viewsuggestion,viewdocument,cspec,adviserquery,clientproedit)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index', index),
    path('about', about,),
    path('contact', contact),
    path('service', service),
    path('countries', country),
    path('login_client',login_client),
    path('adviser',adviser),
    path('registration',registration),
    
    # client url
    path('client',client),
    path('visaadvisor',visaadvisor),
    path('clientadmin',clientadmin),
    path('paymentinfo',paymentinfo),
    path('sendquery',sendquery),
    path('profile',profile),
    path('senddocument',senddocument),
    path('clientlogout',clientlogout),
    path('clientproedit',clientproedit),
    
    
    # adviser url
    path('adindex',adindex),

    path('adclient_profile',adclient_profile),
    path('ad_sendsuggest',ad_sendsuggest),
    # path('adprofile',adprofile),
    path('adview_doc',adview_doc),
    path('adview_recpay',adview_recpay),
    path('adview_sugg',adview_sugg),
    path('login_adviser',login_adviser),
    path('adviserproedit',adviserproedit),
    path('adviserlogout',adviserlogout),
    path('viewsuggestion',viewsuggestion),
    path('viewdocument',viewdocument),
    path('cspec',cspec),
    path('adviserquery',adviserquery),
    
    
    
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

