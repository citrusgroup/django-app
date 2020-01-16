from django.http import HttpResponse, JsonResponse
from propertymatching.models import Company, Agent, ListingItem, User, UserForm, FormMatches
from django.db import connection
from .utils import SendMatchEmail
from propertymatching.mailservice import source

def searchmatch(request):
    if request.method =='POST':
        email_reqs = source.email_source()
        for match_found in email_reqs:
            try:
                email = email_reqs[match_found]['customer']['email']
                SendMatchEmail(email)

            except:
                callback = {"status - bad request", "400"}
                return JsonResponse(callback)
    
    return HttpResponse("/")

