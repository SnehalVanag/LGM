from django import forms
from .models import Franchise, Product

class FranchiseForm(forms.ModelForm):
    class Meta:
        model = Franchise
        fields = ['name', 'address', 'contact_email']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image']