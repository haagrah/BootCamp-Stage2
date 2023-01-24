from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hotels', views.hotel, name='hotels'),
    path('reservationForm/', views.ReservationCreateView.as_view(), name='reservation'),
]
