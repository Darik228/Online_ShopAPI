from django.urls import path, include
from .views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'smartset', SmartPhoneViewSet)
router.register(r'customers', CustomerViewSet)

urlpatterns = [
    path('shop/', CategoryApiList.as_view(), name='Category'),
    path('notebooks/', NotebookApiList.as_view(), name='Notebook'),
    path('smartphones/', SmartPhoneApiList.as_view(), name='SmartPhone'),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]