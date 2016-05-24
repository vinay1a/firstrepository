import django_filters
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import filters
from rest_framework import generics
from django.http import HttpResponse
from geopy.distance import vincenty
import numericalunits as nu
nu.reset_units()
from . import sqdb

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('BusNo', 'BusRoute')


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('BusNo', 'BusRoute')


def GetResults(request):
    q = Snippet.objects.all()
    result = ""
    for r in q:
        result += r.BusNo
        result +=r.BusRoute
        result +=r.latitude
        result +=r.longitude
        result +=r.time
    ti=r.time    
    updated_point = (r.latitude,r.longitude)
    next_point = (13.018778,77.557772)
    print(vincenty(updated_point, next_point).meters)    
    s=float(vincenty(updated_point, next_point).meters)
    speed=300
    time=(s/speed)

          
    return HttpResponse("distance between bus(current position found at time = %s) and busstop is %f meters,and it will reach bus stop by %d minutes" %(ti,s,time))


#caluculating the time