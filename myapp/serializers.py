from rest_framework import serializers
from .models import *


class ComicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comics
        fields = ['id','publisher', 'superhero', 'series', 'issue', 'price']
    # def get_comic_items(self, obj):
    #     comic_query = models.Comics.objects.filter(
    #         comic_id=obj.id)
    #     return comic_query
    
# class ComicsSerializer(serializers.HyperlinkedModelSerializer):

#         class Meta:
#             model = Comics
#             fields = ('id','publisher', 'superhero', 'series', 'issue', 'price')




class PublisherSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Publisher
        fields = ['id','publisher_name', 'address', 'city', 'state',]
    # def get_publisher_items(self, obj):
    #     publisher_query = models.publisher.objects.filter(
    #         publisher_id=obj.id)
    #     return publisher_query
    
# class PublishersSerializer(serializers.HyperlinkedModelSerializer):

#         class Meta:
#             model = Publisher
#             fields = ('id','publisher_name', 'address', 'city', 'state',)

class SuperheroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Superhero
        fields = ['id', 'publisher', 'superhero_name', 'has_comics', 'has_toys']
    # def get_publisher_items(self, obj):
    #     superhero_query = models.superhero.objects.filter(
    #         superhero_id=obj.id)
    #     return superhero_query
    
# class SuperherossSerializer(serializers.HyperlinkedModelSerializer):

#         class Meta:
#             model = Superhero
#             fields = ('id','publisher', 'superhero_name', 'has_comics', 'has_toys')

class ToysSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Toys
        fields = ['id', 'publisher', 'super_hero', 'toy_type', 'toy_name', 'ages']
    # def get_publisher_items(self, obj):
    #     toy_query = models.Toys.objects.filter(
    #         superhero_id=obj.id)
    #     return superhero_query
    
# class SuperherossSerializer(serializers.HyperlinkedModelSerializer):

#         class Meta:
#             model = Superhero
#             fields = ('id','publisher', 'superhero_name', 'has_comics', 'has_toys')