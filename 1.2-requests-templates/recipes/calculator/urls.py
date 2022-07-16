from django.urls import path
from .views import *

urlpatterns = [
    path('omlet/', omlet, name='omlet'),
    path('pasta/', pasta, name='pasta'),
    path('buter/', buter, name='buter'),
]