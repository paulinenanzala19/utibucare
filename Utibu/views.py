from django.shortcuts import render,redirect
from django.http  import HttpResponse, JsonResponse
import json
from django.contrib import messages
from rest_framework import viewsets
from django.template import loader
from .forms import *
from .models import *
import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Utibu(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())

def registerPage(request):
   form= RegistrationForm()
   
   if request.method == 'POST':
     form= RegistrationForm(request.POST)
     if form.is_valid():
        form.save()
        # user = form.cleaned_data.get('username')
        # messages.success(redirect, 'Account was created for' + user)

        return redirect('login')
     
   context = {'form': form}
   return render(request,"django_registration/registration.html",context)

def loginPage(request):
   if request.method == 'POST':
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)
      if user is not None:
         return redirect('service')
   context = {}
   return render(request, "registration/login.html", context)
def about(request):
   return render(request, 'about.html', {})

def service(request):
   return render(request, 'services.html', {})

def medicine(request):
   if request.user.is_authenticated:
      patient = request.user.patient    
      order, created = Order.objects.get_or_create(patient=patient, complete=False)
      meds = order.ordermed_set.all
      cartMeds=order.get_cart_meds

   else:
      meds=[]
      order ={'get_cart_meds':0, 'get_cart_total':0, 'shipping': False}
      cartMeds=['get_cart_meds']

   medicines= Medicine.objects.all()
   context={'medicines': medicines, 'cartMeds': cartMeds}
   return render (request, 'medicine.html', context)

def cart(request):

   if request.user.is_authenticated:
      patient = request.user.patient    
      order, created = Order.objects.get_or_create(patient=patient, complete=False)
      meds = order.ordermed_set.all()
      cartMeds=order.get_cart_meds


   else:
      meds=[]
      order ={'get_cart_meds':0, 'get_cart_total':0, 'shipping': False }
      cartMeds=['get_cart_meds']

 
   context={'meds': meds, 'order':order, 'cartMeds':cartMeds}
   return render (request, 'cart.html', context)

def checkout(request):
   if request.user.is_authenticated:
      patient = request.user.patient    
      order, created = Order.objects.get_or_create(patient=patient, complete=False)
      meds = order.ordermed_set.all()
      cartMeds=order.get_cart_meds


   else:
      meds=[]
      order ={'get_cart_meds':0, 'get_cart_total':0, 'shipping': False}
      cartMeds=['get_cart_meds']

 
   context={'meds': meds, 'order':order, 'cartMeds': cartMeds}
   return render (request, 'checkout.html', context)

def updateMed(request):
   data = json.loads(request.body)
   medicineId = data['medicineId']  
   action = data['action']   
   print('Action:', action)  
   print('Medicine:', medicineId)

   patient = request.user.patient
   medicine=Medicine.objects.get(id=medicineId) 
   order, created = Order.objects.get_or_create(patient=patient, complete=False)
   orderMed, created=OrderMed.objects.get_or_create(order=order, medicine=medicine)   
   if action == 'add':
      orderMed.quantity=(orderMed.quantity + 1)  
   elif action == 'remove':
      orderMed.quantity=(orderMed.quantity - 1)

   orderMed.save()
   if orderMed.quantity <= 0:
      orderMed.delete()

   return JsonResponse('medicine was added', safe=False)

def processOrder(request):
   transaction_id = datetime.datetime.now().timestamp()
   data = json.loads(request.body)
   
   if request.user.is_authenticated:
      patient=request.user.patient
      order, created = Order.objects.get_or_create(patient=patient, complete=False)
      total = float(data['form']['total'])
      order.transaction_id=transaction_id

      if total == order.get_cart_total:
         order.complete = True
      order.save()

      if order.shipping == True:
         ShippingAddress.objects.create(
            patient=patient,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            state=data['shipping']['state']

         )


   else:
      print('User is not logged in')
   return JsonResponse('payment submitted', safe=False)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # serializer_class = UserSerializer