from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"


class NotebookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notebook
        fields = "__all__"


class BaseProductSerializer:

    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    description = serializers.CharField(required=False)
    price = serializers.DecimalField(max_digits=9, decimal_places=2, required=True)
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects)


class SmartphoneSerializer(BaseProductSerializer, serializers.ModelSerializer):

    diagonal = serializers.FloatField(required=True)
    display = serializers.FloatField(required=True)
    model = serializers.CharField(required=True)

    class Meta:
        model = Smartphone
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"