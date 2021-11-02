from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from units import views
urlpatterns = [
    path('available-units/', views.AvailableUnitsList.as_view()),
    path('units/', views.UnitList.as_view()),
    path('units/<int:pk>/', views.UnitDetail.as_view()),

]
