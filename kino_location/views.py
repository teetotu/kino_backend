from django.http import Http404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.decorators import action

from .models import Location
from .serializers import LocationSeralizer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        print(request)
        pk = request.user.id
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class LocationPagination(PageNumberPagination):
    page_size = 10


class LocationViewSet(viewsets.ModelViewSet):
    pagination_class = LocationPagination
    serializer_class = LocationSeralizer
    queryset = Location.objects.all()


class LocationDetails(APIView):

    def get_object(self, id):
        try:
            return Location.objects.get(id=id)
        except Location.DoesNotExist:
            raise Http404

    def get(self, request, my_id, format=None):
        location = self.get_object(id=my_id)
        serializer = LocationSeralizer(location)

        return Response(serializer.data)