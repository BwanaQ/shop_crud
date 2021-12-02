from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Category, Product

class CategoryIndexView(ListView):
    model = Category
    queryset = Category.objects.all()
    template_name = 'shop/category_list.html'
    context_object_name = 'index_category_list'

class CategoryDetailedView(DetailView):
    model = Category
    template_name = 'shop/category_detail_view.html'
    context_object_name = 'category'    

class CategoryCreateView(CreateView):
    model = Category
    success_url = reverse_lazy('category-home')
    fields = ['name', 'slug']
    success_message='The Category was created successfully'    
class CategoryUpdateView(UpdateView):
    model = Category
    success_url = reverse_lazy('category-home')
    fields = ['name', 'slug']
    success_message='The Category was created successfully'

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category-home')
    success_message = "The Category %(name) was deleted successfully!"    



class ProductListView(ListView):
    model = Product
    template_name='product_list.html'
    queryset = Product.objects.order_by('-date_added')

class ProductCreateView(CreateView):
    model = Product
    success_url = reverse_lazy('product-home')
    fields = ['category', 'name', 'slug','description','price', 'image']
    success_message = "Product created successfully!"

class ProductUpdateView(UpdateView):
    model = Product
    success_url = reverse_lazy('product-home')
    fields = ['category', 'name', 'slug','description','price', 'image']
    success_message = "Product updated successfully!"    

class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('product-home')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product-home')
    success_message = "The Product %(name) was deleted successfully!"