from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    user= models.OneToOneField (User, null=True, on_delete=models.CASCADE, blank=True)
    name = models.CharField (max_length=200, null=True)
    email=models.CharField (max_length=200, null=True)

    def _str_(self):
        return self.name
    
class Medicine(models.Model):
    name = models.CharField (max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image= models.ImageField(null=True, blank=True)
    #image

    def _str_(self):
        return self.name
    
    @property #decoretor...access as attribute
    def imageURL(self):
        try:
            url=self.image.url
        except:
            url=''
        return url
    
class Order(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False, null=True, blank=False)
    transaction_id=models.CharField(max_length=100 , null=True)

    def _str_(self):
        return str(self.id)
    
    
    @property
    def get_cart_total(self):
        ordermeds=self.ordermed_set.all()
        total=sum([med.get_total for med in ordermeds])
        return total
    
    @property
    def get_cart_meds(self):
        ordermeds=self.ordermed_set.all()
        total=sum([med.quantity for med in ordermeds])
        return total
    
    @property
    def shipping(self):
        shipping = False
        ordermeds = self.ordermed_set.all()
        for i in ordermeds:
            if i.medicine.digital ==False:
                shipping = True
        return shipping
    
   
    
class OrderMed(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null= True, blank=True)
    date_added=models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.medicine.price * self.quantity
        return total

  
class ShippingAddress(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address=models.CharField(max_length=100 , null=False)
    city=models.CharField(max_length=100 , null=False)
    state=models.CharField(max_length=100 , null=False)
    date_added=models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return self.address













