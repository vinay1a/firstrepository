import django_filters
from django.http import HttpResponse
from geopy.distance import vincenty
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import filters
from rest_framework import generics
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.svm import SVR
import numpy as np


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
    if request.method == 'GET':
       busStopNo = request.GET['val']
       distance = request.GET['distance']
       time = request.GET['time']
       #neural network code..
       f = open('train1.txt','r').readlines()
       x = np.zeros((300,4),dtype=float)
       y=np.zeros((300),dtype=float)
       for i,line in enumerate(f):
       	lone=line.strip('\r\n').strip()
       	if line.count(',')>0:
        	x[i]=[float(p) for p in line.split(',')]
       f2=open('trainout.txt','r').readlines()
       for i,line in enumerate(f2):
           line=line.strip('\r\n')
           y[i]=float(line)
       clf=ExtraTreesRegressor(verbose=0)
       clf.fit(x[:200],y[:200])
       for i in range(200,230):
           yi = clf.predict(x[200:230])
       for i in range(30):
           print (yi[i], y[200+i])
       print ("enter the bus stop number")
       in1=int(raw_input())
       print ("enter the distance")
       in2=int(raw_input())
       print (" enter the day of thr time")
       in3=int(raw_input())
       print ("entr 0.0 for day and 0.1 for night")
       in4=float(raw_input())
       pq=clf.predict([busStopNo,distance,time,0.0])
       print (pq)         



       return HttpResponse("values are " + str (busStopNo) + "  " + str(distance) + " " + str(time)+""+str(pq))
