from rest_framework import serializers
from .models import *


class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class Article_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
