from .views import *
from django.urls import path

urlpatterns = [
    path('get_form/', FormView.as_view(), name='form')
]