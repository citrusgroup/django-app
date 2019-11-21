from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('partner-view/', views.partner_view, name='partner-view'),
    path('form-match/', views.form_match, name='form-match'),
]
