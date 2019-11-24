from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from propertymatching.serializers import UserSerializer, UserFormSerializer, CompanySerializer, AgentSerializer, ListingItemSerializer
from propertymatching.models import User, UserForm, Company, Agent, ListingItem

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserFormViewSet(viewsets.ModelViewSet):
    queryset = UserForm.objects.all()
    serializer_class = UserFormSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class ListingItemViewSet(viewsets.ModelViewSet):
    queryset = ListingItem.objects.all()
    serializer_class = ListingItemSerializer
