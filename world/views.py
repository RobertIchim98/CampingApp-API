from django.http import JsonResponse
from django.shortcuts import render
from .serializers import CampingSpotSerializer
from .models import CampingSpot

from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class TestView(APIView):
    def get(self,request, *args, **kwargs):
        qs = CampingSpot.objects.all()
        serializer = CampingSpotSerializer(qs, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = CampingSpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
