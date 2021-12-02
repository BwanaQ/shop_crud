from django.urls import path
from .views import *
urlpatterns = [
    path('', CategoryIndexView.as_view(), name="home"),
    path('categories/', CategoryIndexView.as_view(), name="category-home"),
    path('new/', CategoryCreateView.as_view(),name='category-create-view'),
    path('category/<slug:slug>/', CategoryDetailedView.as_view(), name="category-detail-view"),
    path('category/<slug:slug>/update/', CategoryUpdateView.as_view(), name="category-update-view"),
    path('category/<slug:slug>/delete/', CategoryDeleteView.as_view(), name="category-delete-view"),

    path('products/', ProductListView.as_view(), name="product-home"),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name="product-detail-view"),
    path('product-new/', ProductCreateView.as_view(),name='product-create-view'),
    path('product/<slug:slug>/update/', ProductUpdateView.as_view(), name="product-update-view"),
    path('product/<slug:slug>/delete/', ProductDeleteView.as_view(), name="product-delete-view"),

]