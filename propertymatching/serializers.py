from rest_framework import serializers

from propertymatching.models import User, UserForm, Company, Agent, ListingItem

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'phone_number', 'email', 'created_at', 'updated_at')

class UserFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserForm
        fields = ('budget_min', 'budget_max', 'monthly_cost_min', 'monthly_cost_max', 'properties', 'user', 'created_at', 'updated_at')

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'phone_number', 'email', 'created_at', 'updated_at')

class AgentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Agent
        fields = ('name', 'phone_number', 'email', 'company', 'created_at', 'updated_at')

class ListingItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ListingItem
        fields = ('name', 'price', 'monthly_cost', 'agent', 'properties', 'created_at', 'updated_at')
