from django.urls import path
from .views import load_dummy_data

urlpatterns = [
    path('load-dummy-data/', load_dummy_data),
]