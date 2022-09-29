from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class CategoryApiList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NotebookApiList(ListAPIView):
    queryset = Notebook.objects.all()
    serializer_class = NotebookSerializer


class SmartPhoneApiList(ListAPIView):
    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    filter_backends = [SearchFilter]
    search_fields = ['model']

    def get_queryset(self):
        queryset = Smartphone.objects.order_by('-price')
        return queryset


class SmartPhoneViewSet(ModelViewSet):

    queryset = Smartphone.objects.all()
    serializer_class = SmartphoneSerializer
    filter_backends = [SearchFilter]
    search_fields = ['model']
    permission_classes = [IsAuthenticated]


class CustomerViewSet(ModelViewSet):

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer