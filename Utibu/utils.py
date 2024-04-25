import json
from .models import *

def cookieCart(request):
    try:

         cart=json.loads(request.COOKIES['cart'])
    except:
         cart={}
    print('Cart:', cart)
    meds=[]
    order ={'get_cart_meds':0, 'get_cart_total':0, 'shipping': False }
    cartMeds = order['get_cart_meds']

    for i in cart:
         try:

            cartMeds += cart[i]['quantity']

            medicine = Medicine.objects.get(id=i)
            total= (medicine.price * cart[i]["quantity"])
            order['get_cart_total'] += total
            order['get_cart_meds'] += cart[i]["quantity"]

            med={
               'medicine':{
                  'id': medicine.id,
                  'name': medicine.name,
                  'price':medicine.price,
                  'imageURL': medicine.imageURL,
                  },
               'quantity':cart[i]["quantity"],
               'get_total': total
               }
            meds.append(med)

            if medicine.digital==False:
               order['shipping']=True

         except:
            pass

    return {'cartMeds': cartMeds, 'order': order, 'meds':meds}

def cartData(request):
    if request.user.is_authenticated:
      patient = request.user    
      order, created = Order.objects.get_or_create(patient=patient, complete=False)
      meds = order.ordermed_set.all()
      cartMeds=order.get_cart_meds


    else:
      cookieData = cookieCart(request)
      cartMeds=cookieData['cartMeds']
      order=cookieData['order']
      meds=cookieData['meds']
    return{'cartMeds': cartMeds, 'order': order, 'meds':meds}

def guestOrder(request, data):
    print('User is not logged in')
    print('COOKIES:',request.COOKIES)
    name=data['form']['name']
    
    email=data['form']['email']

    cookieData=cookieCart(request)
    meds=cookieData['meds']

    patient, created = Patient.objects.get_or_create(
        email=email,
      )
    patient.name = name
    patient.save()

    order= Order.objects.create(
        patient=patient,
        complete= False,
      )

    for med in meds:
         medicine=Medicine.objects.get(id=med['medicine']['id'])
         orderMed=OrderMed.objects.create(
            medicine=medicine,
            order=order,
            quantity=med['quantity']
         )
    return patient, order