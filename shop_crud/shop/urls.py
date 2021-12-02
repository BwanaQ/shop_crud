from django.urls import path
from .views import *
urlpatterns = [
    path('', CategoryIndexView.as_view(), name="home"),
]