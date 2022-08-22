from rest_framework import serializers
from .models import *


class ComicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comics
        fields = ['id','publisher', 'superhero', 'series', 'issue', 'price']





class PublisherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = ['id','publisher_name', 'address', 'city', 'state',]


class SuperheroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Superhero
        fields = ['id', 'publisher', 'superhero_name', 'has_comics', 'has_toys']


class ToysSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Toys
        fields = ['id', 'publisher', 'super_hero', 'toy_type', 'toy_name', 'ages']
