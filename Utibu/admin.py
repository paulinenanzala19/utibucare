from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Medicine)
admin.site.register(Order)
admin.site.register(OrderMed)
admin.site.register(ShippingAddress)