from django.urls import path, include
from nomad_auto_advert.cars.views import CarTypeView, CarMarkView, CarModelView, CarGenerationView, CarSerieView, \
    CarModificationView, CarCharacteristicView, CarCharacteristicValueView, CarEquipmentView, \
    CarOptionView, CarOptionValueView, CarViewSet, CarDetailView, CarColorView, MultipleOptionView, CustomOptionViewSet, \
    CustomOptionListView
from rest_framework import routers

app_name = 'cars'
router = routers.DefaultRouter()
router.register('custom-options', CustomOptionViewSet, basename='custom-options')
router.register('', CarViewSet, basename='cars')

urlpatterns = [
    path('colors/', CarColorView.as_view()),
    path('types/', CarTypeView.as_view()),
    path('marks/', CarMarkView.as_view()),
    path('models/', CarModelView.as_view()),
    path('generations/', CarGenerationView.as_view()),
    path('series/', CarSerieView.as_view()),
    path('modifications/', CarModificationView.as_view()),
    path('car-characteristics/', CarCharacteristicView.as_view()),
    path('car-characteristic-values/', CarCharacteristicValueView.as_view()),
    path('equipment/', CarEquipmentView.as_view()),
    path('options/', CarOptionView.as_view()),
    path('option-values/', CarOptionValueView.as_view()),
    path('options/list/', CustomOptionListView.as_view()),

    path('multiple-options/', MultipleOptionView.as_view()),

    path('detail/<int:id>/', CarDetailView.as_view()),
    path('', include(router.urls)),

]
