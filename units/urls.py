from django.urls import path

from units import views
urlpatterns = [
    path('available-units/', views.AvailableUnitsList.as_view()),
]
