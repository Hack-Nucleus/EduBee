from django.contrib import admin
from django.urls import path
from Payments import views
 
urlpatterns = [
    path('', views.homepage, name='index'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('admin/', admin.site.urls),
]