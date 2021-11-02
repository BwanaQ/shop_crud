from rest_framework.response import Response
from rest_framework.views import APIView
from units.models import Unit
from units.serializers import UnitSerializer
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS


class UnitWritePermission(BasePermission):
    message = 'Rights restricted to unit creator only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user


class AvailableUnitsList(APIView):
    def get(self, request, format=None):
        units = Unit.objects.filter(occupied=False)
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)


class UnitList(generics.ListCreateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Unit.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UnitDetail(generics.RetrieveUpdateDestroyAPIView, UnitWritePermission):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (IsAuthenticated, UnitWritePermission,)

    def get_queryset(self):
        return Unit.objects.filter(owner=self.request.user)
