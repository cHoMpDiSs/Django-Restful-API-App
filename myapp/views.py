from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import renderers

from .serializers import *
from .models import Comics, Publisher, Toys, Superhero
# Create your views here.
def home(request):
    return render(request, 'home.html')

def comics(request):
    return render(request, 'comics.html')

def thankyou(request):
    return render(request, 'thankyou.html')

#  ==============================================
# Comics api functions

class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comics.objects.all()
    serializer_class = ComicSerializer

class ComicApiView(APIView):
   
    def get(self, request,comic_id=None, *args, **kwargs):
    
        if comic_id == None:
            comics = Comics.objects.all()
            serializer = ComicSerializer(comics, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            comic_instance = Comics.objects.get(id=comic_id)
            serializer = ComicSerializer(comic_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

        
    def post(self, request, *args, **kwargs):
        '''
        Create the Comic with given comic data
        '''
        data = {
            'publisher': request.data.get('publisher'), 
            'superhero' : request.data.get('superhero'),
            'series' : request.data.get('series'),
            'issue' :request.data.get('issue'),
            'price':request.data.get('price')          
        }
        
        serializer = ComicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, comic_id, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''
        comic_instance = Comics.objects.get(id=comic_id)
        if not comic_instance:
            return Response(
                {"res": "Object with comic id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'publisher': request.data.get('publisher'), 
            'superhero' : request.data.get('superhero'),
            'series' : request.data.get('series'),
            'issue' :request.data.get('issue'),
            'price':request.data.get('price')          
        }
        serializer = ComicSerializer(instance = comic_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, comic_id, *args, **kwargs):
        '''
        Deletes the comic with given comic_id if exists
        '''
        comic_instance = Comics.objects.get(id=comic_id)
        if not comic_instance:
            return Response(
                {"res": "Object with comic id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        comic_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


# Publisher api functions

class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class PublisherApiView(APIView):

    def get(self, request,publisher_id=None, *args, **kwargs):

        if publisher_id == None:
            publishers = Publisher.objects.all()
            serializer = PublisherSerializer(publishers, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            publisher_instance = Publisher.objects.get(id=publisher_id)
            serializer = PublisherSerializer(publisher_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Publisher with given Publisher data
        '''
        data = {
            'publisher_name': request.data.get('publisher_name'), 
            'address' : request.data.get('address'),
            'city' : request.data.get('city'),
            'state' :request.data.get('state')        
        }
        
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, publisher_id, *args, **kwargs):
        '''
        Updates the publisher item with given publisher_id if exists
        '''
        publisher_instance = Publisher.objects.get(id=publisher_id)
        if not publisher_instance:
            return Response(
                {"res": "Object with publisher id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'publisher_name': request.data.get('publisher_name'), 
            'address' : request.data.get('address'),
            'city' : request.data.get('city'),
            'state' :request.data.get('state')
                    
        }
        serializer = PublisherSerializer(instance = publisher_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, comic_id, *args, **kwargs):
        '''
        Deletes the publisher with given publisher_id if exists
        '''
        publisher_instance = Publisher.objects.get(id=publisher_id)
        if not publisher_instance:
            return Response(
                {"res": "Object with publisher id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        publisher_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )
# Superhero api functions
class SuperheroViewSet(viewsets.ModelViewSet):
    queryset = Superhero.objects.all()
    serializer_class = SuperheroSerializer

class SuperheroApiView(APIView):

    def get(self, request,superhero_id=None, *args, **kwargs):

        if superhero_id == None:
            superheros = Superhero.objects.all()
            serializer = SuperheroSerializer(superheros, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            superhero_instance = Superhero.objects.get(id=superhero_id)
            serializer = SuperheroSerializer(superhero_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Superhero with given Superhero data
        '''
        data = {
            'publisher': request.data.get('publisher'), 
            'superhero_name' : request.data.get('superhero_name'),
            'has_comics' : request.data.get('has_comics'),
            'has_toys' :request.data.get('has_toys')        
        }
        
        serializer = SuperheroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, superhero_id, *args, **kwargs):
        '''
        Updates the Superhero with given superhero_id if exists
        '''
        superhero_instance = Superhero.objects.get(id=superhero_id)
        if not superhero_instance:
            return Response(
                {"res": "Object with superhero id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'publisher': request.data.get('publisher'), 
            'superhero_name' : request.data.get('superhero_name'),
            'has_comics' : request.data.get('has_comics'),
            'has_toys' :request.data.get('has_toys') 
                    
        }
        serializer = SuperheroSerializer(instance = superhero_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, comic_id, *args, **kwargs):
        '''
        Deletes the Superhero with given superhero id if exists
        '''
        superhero_instance = Superhero.objects.get(id=superhero_id)
        if not superhero_instance:
            return Response(
                {"res": "Object with superhero id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        superhero_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )

# Toys api functions

class ToysViewSet(viewsets.ModelViewSet):
    queryset = Toys.objects.all()
    serializer_class = ToysSerializer

class ToysApiView(APIView):

    def get(self, request,toy_id=None, *args, **kwargs):

        if toy_id == None:
            toys = Toys.objects.all()
            serializer = ToysSerializer(toys, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            toy_instance = Toys.objects.get(id=toy_id)
            serializer = ToysSerializer(toy_instance)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        '''
        Create the Toy with given Toys data
        '''
        data = {
            'publisher:': request.data.get('publisher'), 
            'super_hero': request.data.get('super_hero'), 
            'toy_type' : request.data.get('toy_type'),
            'toy_name' : request.data.get('toy_name'),
            'ages' :request.data.get('ages')        
        }
        
        serializer = ToysSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, toy_id, *args, **kwargs):
        '''
        Updates the Toy with given toy_id if exists
        '''
        toy_instance = Toys.objects.get(id=toys_id)
        if not toy_instance:
            return Response(
                {"res": "Object with toy id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'publisher:': request.data.get('publisher'),
            'super_hero': request.data.get('super_hero'), 
            'toy_type' : request.data.get('toy_type'),
            'toy_name' : request.data.get('toy_name'),
            'ages' :request.data.get('ages') 
                    
        }
        serializer = ToysSerializer(instance = toy_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, toy_id, *args, **kwargs):
        '''
        Deletes the Toy with given toy id if exists
        '''
        toy_instance = Toys.objects.get(id=toy_id)
        if not toy_instance:
            return Response(
                {"res": "Object with toy id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        toy_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


