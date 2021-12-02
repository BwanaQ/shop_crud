from django.forms import ModelForm
from .models import Category, Product

class CategoryCreateForm(ModelForm):
    class Meta:
        model = Category


class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['date_added','thumbnail']