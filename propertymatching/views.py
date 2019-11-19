from django.http import HttpResponse
from django.http import JsonResponse
def index(request):
    return HttpResponse("Hello from the property matching app")

def partnerView(request):
    return HttpResponse("partner view")


def form_match(request):
    


    return JsonResponse(data)
