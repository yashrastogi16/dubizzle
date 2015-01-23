from django.shortcuts import render
from serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from feeds.models import *
# Create your views here.

@api_view(['GET', 'POST'])
def daily(request):
	if request.method == 'GET':
		property_daily = dubizzle.objects.all()
		serializer = dubizzleSerializer(property_daily, many=True)
		return Response(serializer.data)

@api_view(['GET', 'POST'])
def hourly(request):
	if request.method == 'GET':
		property_daily = dubizzle.objects.all()
		serializer = dubizzleSerializer(property_daily, many=True)
		return Response(serializer.data)

@api_view(['GET', 'POST'])
def feed(request):
	if request.method == 'GET':
		property_daily = dubizzle.objects.all()
		serializer = dubizzleSerializer(property_daily, many=True)
		return Response(serializer.data)