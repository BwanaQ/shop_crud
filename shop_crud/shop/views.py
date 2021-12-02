from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Category, Product
from django.contrib.messages.views import SuccessMessageMixin

"""
crud views
"""
class CategoryIndexView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'shop/category_list.html'
    context_object_name = 'index_category_list'

class CategoryDetailedView(DetailView):
    model = Category
    template_name = 'shop/category_detail_view.html'
    context_object_name = 'category'    

class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    success_url = reverse_lazy('category-home')
    fields = ['name', 'slug']
    success_message='The category was created successfully'    
class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    success_url = reverse_lazy('category-home')
    fields = ['name', 'slug']
    success_message='The category was updated successfully'

class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('category-home')
    success_message = "The category was deleted successfully!"    



class ProductListView(ListView):
    model = Product
    template_name='product_list.html'
    queryset = Product.objects.order_by('-date_added')

class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    success_url = reverse_lazy('product-home')
    fields = ['category', 'name', 'slug','description','price', 'image']
    success_message = "Product created successfully!"

class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    success_url = reverse_lazy('product-home')
    fields = ['category', 'name', 'slug','description','price', 'image']
    success_message = "Product updated successfully!"    

class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('product-home')


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('product-home')
    success_message = "The Product %(name) was deleted successfully!"