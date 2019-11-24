from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello from the property matching app")

def partner_view(request):
    return HttpResponse("partner view")


def form_match(request):
    return HttpResponse("form view")
