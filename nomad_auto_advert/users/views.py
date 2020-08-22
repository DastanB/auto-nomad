from django.contrib.auth import get_user_model
import logging

from rest_framework import generics, viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from nomad_auto_advert.users.serializers import NativeUserSerializer, GarageProfileSerializer, ContactPhoneSerializer
from nomad_auto_advert.users.models import Profile, ContactPhone
from nomad_auto_advert.utils.mixins import MultiSerializerViewSetMixin

logger = logging.getLogger(__name__)


User = get_user_model()


class UserListDebug(generics.ListAPIView):
    serializer_class = NativeUserSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    queryset = User.objects.all()


class GarageProfileViewSet(MultiSerializerViewSetMixin, viewsets.ReadOnlyModelViewSet):
    serializer_class = GarageProfileSerializer
    permission_classes = (AllowAny, )
    pagination_class = None

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)


class ContactPhoneViewSet(viewsets.ModelViewSet):
    serializer_class = ContactPhoneSerializer

    def get_queryset(self):
        return ContactPhone.objects.filter(profile=self.request.user)

    def perform_create(self, serializer):
        serializer.save(profile=self.request.user)
