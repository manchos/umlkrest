from django.contrib.gis.db.models.functions import Distance
from django.shortcuts import render
from api.models import Object
from api.serializers import ObjectSerializer
from django.contrib.gis.geos import GEOSGeometry
from rest_framework import generics
from django.http import HttpResponse
import geocoder


class ListCreateObjects(generics.ListCreateAPIView):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer

    def perform_create(self, serializer):
        address = serializer.initial_data['address']
        g = geocoder.yandex(address)
        latitude = g.latlng[0]
        longitude = g.latlng[1]
        pnt = 'POINT({} {})'.format(str(longitude), str(latitude))
        serializer.save(location=pnt)


    def get_queryset(self):
        qs = super().get_queryset()
        latitude = self.request.query_params.get('lat', None)
        longitude = self.request.query_params.get('lng', None)

        if latitude and longitude:
            pnt = GEOSGeometry(
                'POINT({} {})'.format(str(longitude), str(latitude)),
                srid=4326
            )
            qs = qs.annotate(
                distance=Distance('location', pnt)).order_by('distance')

        return qs


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.
