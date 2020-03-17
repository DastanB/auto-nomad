from django.urls import path
from rest_framework import routers
from nomad_auto_advert.advert.views import ColorListView

app_name = 'advert'

router = routers.DefaultRouter()


urlpatterns = (
    path(r'colors/', ColorListView.as_view()),
)
