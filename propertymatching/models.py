from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    phone_number = models.TextField(max_length=20)
    company_email = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Agent(models.Model):
    agent_name = models.CharField(max_length=50)
    phone_number = models.TextField(max_length=20)
    agent_email = models.TextField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Listing_item(models.Model):
    listing_name = models.CharField(max_length=50)
    price = models.TextField(max_length=20)
    monthly_cost = models.TextField(max_length=20)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    properties = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



