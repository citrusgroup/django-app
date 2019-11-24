from django.contrib import admin
from .models import User, UserForm, Company, Agent, ListingItem

# Register your models here.
admin.site.register(User)
admin.site.register(UserForm)
admin.site.register(Company)
admin.site.register(Agent)
admin.site.register(ListingItem)
