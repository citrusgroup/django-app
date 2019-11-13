from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('partner-view/', views.partnerView, name='partner-view')
]
