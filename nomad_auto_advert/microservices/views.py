from django.http import Http404, HttpResponse
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from nomad_auto_advert.cars.models import Car
from nomad_auto_advert.cars.serializers import CarUpdateSerializer, CarSerializer
from nomad_auto_advert.microservices.models import Service
from nomad_auto_advert.microservices.permissions import HasAPIKey
from nomad_auto_advert.microservices.serializers import MicroServiceSerializer
import logging

from nomad_auto_advert.microservices.utils import update_car

logger = logging.getLogger(__name__)


class ServicesViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = MicroServiceSerializer
    queryset = Service.objects.all()


def health_check_view(request):
    return HttpResponse()


class UpdateCarView(APIView):
    permission_classes = (HasAPIKey, )

    def post(self, request, *args, **kwargs):
        car = update_car(data=request.data)
        data = CarSerializer(car).data
        print(f"Data: {data}")
        return Response(data)
