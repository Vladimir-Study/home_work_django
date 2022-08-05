from django.urls import path
from .views import SensorView, SensorUpdate, MeasurementCreate, SensorDetailView


urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensor/<int:pk>/', SensorDetailView.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
