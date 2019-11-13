from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from the property matching app")

def partnerView(request):
    return HttpResponse("partner view")
