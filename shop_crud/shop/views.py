from django.views.generic import ListView
from .models import Category, Product

class CategoryIndexView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'shop/category_list.html'
    context_object_name = 'index_category_list'