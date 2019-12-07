import datetime

from django.contrib.postgres.fields import JSONField
from django.db import models

# Partner models
class Company(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.TextField(max_length=20, null=True)
    email = models.TextField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Agent(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone_number = models.TextField(max_length=20, null=True)
    email = models.TextField(max_length=100, null=True)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ListingItem(models.Model):
    name = models.CharField(max_length=50)
    price = models.TextField(max_length=20)
    monthly_cost = models.TextField(max_length=20)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)
    properties = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# User models
class User(models.Model):
    hubspot_vid = models.IntegerField(null=True, unique=True)
    hubspot_updated_at = models.DateTimeField(null=True, auto_now=False)
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class UserForm(models.Model):
    budget_min = models.FloatField(null=True)
    budget_max = models.FloatField(null=True)
    monthly_cost_min = models.FloatField(null=True)
    monthly_cost_max = models.FloatField(null=True)
    properties = JSONField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
