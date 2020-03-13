from django.contrib.auth import get_user_model
import logging

from rest_framework import generics, viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from nomad_auto_advert.users.serializers import NativeUserSerializer, GarageProfileSerializer
from nomad_auto_advert.users.models import Profile
from nomad_auto_advert.utils.mixins import MultiSerializerViewSetMixin

logger = logging.getLogger(__name__)


User = get_user_model()


class UserListDebug(generics.ListAPIView):
    serializer_class = NativeUserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    queryset = User.objects.all()


class GarageProfileViewSet(MultiSerializerViewSetMixin, viewsets.ModelViewSet):
    serializer_class = GarageProfileSerializer
    permission_classes = (AllowAny, )
    pagination_class = None
    queryset = Profile.objects.all()
