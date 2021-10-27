from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Unit
from .serializers import UnitSerializer


class AvailableUnitsList(APIView):
    def get(self, request, format=None):
        units = Unit.objects.filter(occupied=False)
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)
