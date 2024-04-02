from django.urls import path,include
from . import views
from django.conf.urls.static import static
from .views import *
from django.conf import settings
from rest_framework import routers
from django.contrib.auth import views as auth_views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns=[
    path('',views.home, name='home'),
    path('api/', include(router.urls)),
    path('accounts/register', views.registerPage, name="register"),
    path('accounts/login', views.loginPage, name="login"),
    path('about.html', views.about, name='about'),
    path('services.html', views.service, name="service"),
    path('medicine.html', views.medicine, name="medicine"),
    path('cart.html', views.cart, name="cart"),
    path('checkout.html', views.checkout, name="checkout"),
    path('update_med/', views.updateMed, name="update_med"),
    path('process_order/', views.processOrder, name="process_order")
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)