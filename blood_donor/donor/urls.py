from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('register/', views.donor_register, name='donor_register'),
    path('request/', views.blood_request, name='blood_request'),
    path('list/', views.donor_list, name='donor_list'),
    path('request/',views.blood_request_success,name='blood_request_success')
]