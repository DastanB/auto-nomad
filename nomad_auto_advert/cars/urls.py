from django.urls import path, include
from nomad_auto_advert.cars.views import CarTypeView, CarMarkView, CarModelView, CarGenerationView, CarSerieView, \
    CarModificationView, CarCharacteristicView, CarCharacteristicValueView, CarEquipmentView, \
    CarOptionView, CarOptionValueView, CarViewSet
from rest_framework import routers

app_name = 'cars'
router = routers.DefaultRouter()
router.register(r'', CarViewSet, basename='cars')

urlpatterns = [
    path('types/', CarTypeView.as_view()),
    path('marks/', CarMarkView.as_view()),
    path('models/', CarModelView.as_view()),
    path('generations/', CarGenerationView.as_view()),
    path('series/', CarSerieView.as_view()),
    path('modifications/', CarModificationView.as_view()),
    path('car-characteristics', CarCharacteristicView.as_view()),
    path('car-characteristic-values', CarCharacteristicValueView.as_view()),

    path('equipment/', CarEquipmentView.as_view()),
    path('options/', CarOptionView.as_view()),
    path('option-values/', CarOptionValueView.as_view()),

    path('', include(router.urls)),

]
