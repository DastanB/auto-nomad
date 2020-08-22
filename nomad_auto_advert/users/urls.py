from django.urls import path
from rest_framework import routers

from nomad_auto_advert.users import views

app_name = "users"

router = routers.DefaultRouter()
router.register('profile', views.GarageProfileViewSet, 'profile')
router.register('phones', views.ContactPhoneViewSet, basename='phones')

urlpatterns = [
    path('all/', views.UserListDebug.as_view())
]

urlpatterns += router.urls
