"""citrusgroup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from propertymatching.models import User, UserForm
from rest_framework import routers

from propertymatching.view_sets import UserViewSet, UserFormViewSet, CompanyViewSet, AgentViewSet, ListingItemViewSet

router = routers.DefaultRouter()
router.register(r'api/v1/users', UserViewSet)
router.register(r'api/v1/user-forms', UserFormViewSet)
router.register(r'api/v1/companies', CompanyViewSet)
router.register(r'api/v1/agents', AgentViewSet)
router.register(r'api/v1/listing-items', ListingItemViewSet)

# router.register(r'api/v1/type-form/register-form', TypeFormReceiverView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework')),
    path('property-matching/', include('propertymatching.urls')),
]
