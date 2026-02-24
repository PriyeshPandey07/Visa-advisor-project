from django.shortcuts import render,redirect
from django.urls import reverse
from desire.models import Client,VisaAdvisor,customerquerry,ClientDocument,Contact,Adviserquerry
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout as auth_logout
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.conf import settings
from .backends import ClientAuthenticationBackend,VisaAdvisorBackend
from django.contrib.auth.decorators import login_required
from desire.forms import ClientEditProForm,AdviserEditForm
from django.db.models import Q

def index(request):   
    if request.method == "POST":
        # Retrieve data from POST request
        first_name = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        email = request.POST.get("email", "")
        phonenumber = request.POST.get("pn", 0)  # Assuming default as 0 or handle conversion/validation properly
        message = request.POST.get("message", "")
        
        # Create and save the contact instance
        x = Contact.objects.create(
            first_name=first_name,
            last_name=lname,
            email=email,
            phonenumber=phonenumber,  # Ensure this is properly converted to an int if necessary
            message=message
        )
        x.save()
    return render(request,"index.html")


def cspec(request):
    reviews = []  # Initialize an empty list for cases when query is None or an empty string
    if request.method == "GET":
        query = request.GET.get('search', '')  # Provide a default empty string if 'search' is not provided
        if query:  # This checks if query is not an empty string
            reviews = VisaAdvisor.objects.filter(country_specialization__icontains=query)
        else:
            # Optional: Handle the case when query is empty, e.g., return all advisors or a subset
            # reviews = VisaAdvisor.objects.all()  # Example: Uncomment to return all advisors if no query
            pass

        data = {'reviews': reviews}
        # The print statements seem to be for debugging purposes, you can remove them or keep them as needed
        print(query)
        print(reviews)
       
    return render(request, "cspec.html", data)

def contact(request):
    if request.method == "POST":
        # Retrieve data from POST request
        first_name = request.POST.get("fname", "")
        lname = request.POST.get("lname", "")
        email = request.POST.get("email", "")
        phonenumber = request.POST.get("pn", 0)  # Assuming default as 0 or handle conversion/validation properly
        message = request.POST.get("message", "")
        
        # Create and save the contact instance
        x = Contact.objects.create(
            first_name=first_name,
            last_name=lname,
            email=email,
            phonenumber=phonenumber,  # Ensure this is properly converted to an int if necessary
            message=message
        )
        x.save()
    return render(request,"contact.html")
def service(request):
    return render(request,"service.html")
def about(request):
    return render(request,"about.html")
def country(request):
    
    return render(request,"countries.html")
   
def registration(request):
    return render(request,"registration.html")

def adviser(request):
    return render(request,"adviser.html")

def client(request):
    if request.method=="POST":
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        address=request.POST.get("address")
        dob=request.POST.get("dob")
        phonenumber=request.POST.get("phonenumber")
        
        # Client.objects.create()
        # my_user=User.objects.create_user(username,password)
        # my_user.save()
        
        Client.objects.create(
            username=username,
            email=email,
            password=password,
            address=address,
            dob=dob,
            phoneno=phonenumber)

        return redirect(login_client)
    
    return render(request,"registration.html")
                  
def login_client(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user using custom authentication backend
        backend = ClientAuthenticationBackend()
        user = backend.authenticate(request, username=username, password=password)
        
        if user is not None:
            # Set the backend attribute before logging in
            user.backend = 'desire.backends.ClientAuthenticationBackend'
            login(request, user)
            return redirect(clientadmin)
        else:
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html') 

def clientlogout(request):
    auth_logout(request)
    return redirect(login_client)

def visaadvisor(request):
    if request.method=="POST":
        username=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        experience=request.POST.get("experience")
        country_specialization=request.POST.get("country_specialization")
        phoneno=request.POST.get("phoneno")
        education=request.POST.get("education")
        
        # Client.objects.create()
        VisaAdvisor.objects.create(
            username=username,
            email=email,
            password=password,
            experience=experience,
            country_specialization=country_specialization,
            phoneno=phoneno,
            education=education
            )

        return redirect(login_adviser)   
    return render(request,"registration.html")

@login_required(login_url=login_client)
def clientadmin(request):
    client_id = request.user.id  # Get the id of the currently logged in client
    client = Client.objects.get(id=client_id) 
    return render(request,"clientadmin/index.html",{"client":client})
    
@login_required(login_url=login_client)
def paymentinfo(request):
    return render(request,"clientadmin/payment-info.html")

@login_required(login_url=login_client)
def sendquery(request):
    if request.method=="POST":
        email=request.POST['email']
        query=request.POST['query']
        x=customerquerry.objects.create(email=email,query=query)
        x.save()
    return render(request,"clientadmin/send-query.html")

@login_required(login_url=login_client)
def senddocument(request):
    client_id = request.user.id  # Get the id of the currently logged in client
    client = Client.objects.get(id=client_id) 
    if request.method=="POST":
        email = request.POST.get('email')
        aadharcard = request.FILES.get('aadharcard')
        paancard = request.FILES.get('paancard')
        passport = request.FILES.get('passport')
        
        y=ClientDocument.objects.create(email=email,aadharcard=aadharcard,paancard=paancard,passport=passport)
        y.save()
    return render(request,"clientadmin/send-document.html",{"client":client})


@login_required(login_url=login_client)
def profile(request):
    client_id = request.user.id  # Get the id of the currently logged in client
    client = Client.objects.get(id=client_id) 
    return render(request,"clientadmin/profile.html", {'client': client})

def clientproedit(request):
    client_id = request.user.id
    xyz = Client.objects.get(id=client_id)

    if request.method == 'POST':
        form = ClientEditProForm(request.POST, instance=xyz)
        if form.is_valid():
            form.save()
            # Use reverse to get the URL for 'profile' view and then redirect
            return redirect(reverse(profile))  # Replace 'profile' with the actual name of your profile view
    else:
        form = ClientEditProForm(instance=xyz)
    
    # Use render to return the response with your template and context
    return render(request, "clientadmin/clientproedit.html", {'form': form})


# adviser

def login_adviser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user using custom authentication backend
        backend = VisaAdvisorBackend()
        user = backend.authenticate(request, username=username, password=password)
        
        if user is not None:
            # Set the backend attribute before logging in
            user.backend = 'desire.backends.VisaAdvisorBackend'
            login(request, user)
            return redirect(adindex)
        else:
            return render(request, 'adviser.html', {'error_message': 'Invalid credentials'})
    return render(request, 'adviser.html')

@login_required(login_url=login_adviser)
def adindex(request):
    x=Client.objects.all() 
    y=x.count()
    return render(request,"adviseradmin/index.html",{"y":y})
     
@login_required(login_url=login_adviser)
def adclient_profile(request):
    ru=Client.objects.all()  
    return render(request,"adviseradmin/client-profile.html",{"ru":ru})

@login_required(login_url=login_adviser)
def ad_sendsuggest(request):
    return render(request,"adviseradmin/send-suggestions.html")

# def adprofile(request):
#     adviser=request.user
#     return render(request,"adviseradmin/users-profile.html",{"adviser":adviser})

@login_required(login_url=login_adviser)
def adview_doc(request):
    return render(request,"adviseradmin/view-documents.html")

@login_required(login_url=login_adviser)
def adview_recpay(request):
    return render(request,"adviseradmin/view-receive-payment.html")

@login_required(login_url=login_adviser)
def adview_sugg(request):
    return render(request,"adviseradmin/view-suggestions.html")



@login_required(login_url=login_adviser)
def adviserproedit(request):
    adviser=request.user
    client_id = request.user.id
    xyz = VisaAdvisor.objects.get(id=client_id)

    if request.method == 'POST':
        form = AdviserEditForm(request.POST, instance=xyz)
        if form.is_valid():
            form.save()
            # Use reverse to get the URL for 'profile' view and then redirect
            return redirect(reverse(adviserproedit))  # Replace 'profile' with the actual name of your profile view
    else:
        form = AdviserEditForm(instance=xyz)
    
    # Use render to return the response with your template and context
    return render(request, "adviseradmin/users-profile.html", {'form': form,'adviser':adviser})

@login_required(login_url=login_adviser)
def adviserlogout(request):
    auth_logout(request)
    return redirect(login_adviser)

@login_required(login_url=login_adviser)
def viewsuggestion(request):
    data = None  # Initialize data outside the if block
           
    user_adviser_id = request.user.id
    data = customerquerry.objects.filter(adviser_id=user_adviser_id)     
    return render(request, "adviseradmin/view-suggestions.html", {"data": data})

@login_required(login_url=login_adviser)
def viewdocument(request):
    user_adviser_id = request.user.id
    data = ClientDocument.objects.filter(adviser_id=user_adviser_id)     
    return render(request, "adviseradmin/view-documents.html", {"data": data})

@login_required(login_url=login_adviser)
def adviserquery(request):
    if request.method=="POST":
        email=request.POST['email']
        query=request.POST['query']
        x=Adviserquerry.objects.create(email=email,query=query)
        x.save()
    return render(request,"adviseradmin/send-suggestions.html")

