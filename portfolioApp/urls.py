from django.urls import path
from portfolioApp import views



urlpatterns = [
    path('', views.about, name='about'),
]