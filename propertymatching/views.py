from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpRequest
import requests
from django.conf import settings
import environ
from pprint import pprint
from propertymatching.models import User, UserForm

def index(request):
    return HttpResponse("Hello from the property matching app")

def partner_view(request):
    return HttpResponse("partner view")


def form_match(request):
    return HttpResponse("form view")

def get_hubspot_customers(request):
    response = requests.get('https://api.hubapi.com/contacts/v1/lists/recently_updated/contacts/recent?hapikey=a995863c-2ef2-4c84-bc7e-10f5ea7716c9')
    contacts = response.json()
    for contact in contacts['contacts']:
        vid = contact['canonical-vid']
        addedAt = contact['addedAt']
        thisUser = User.objects.filter(
                hubspot_vid=vid
            ).exclude(
                hubspot_updated_at__gte=addedAt
            )

    contact = requests.get('https://api.hubapi.com/contacts/v1/contact/vid/151/profile?hapikey=a995863c-2ef2-4c84-bc7e-10f5ea7716c9')
    # return HttpResponse(contacts['contacts'])
    return JsonResponse(contacts['contacts'][0], safe=False)
