from django import forms
from .models import Franchise, Product 
from .models import Staff


class FranchiseForm(forms.ModelForm):
    class Meta:
        model = Franchise
        fields = ['name', 'address', 'contact_email']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'discount', 'description']
        widgets = {
            'discount': forms.NumberInput(attrs={
                'min': 0,
                'max': 100,
                'step': '0.01',
                'placeholder': 'Enter discount (%)'
            }),
        }
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'email', 'phone']





# 

# 

# from django import forms
# from .models import Franchise, Product ,Category
# from .models import Staff


# class FranchiseForm(forms.ModelForm):
#     class Meta:
#         model = Franchise
#         fields = ['name', 'address', 'contact_email']

# class ProductForm(forms.ModelForm):
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         widget=forms.Select(attrs={'class': 'form-select'}),
#         required=True,
#         label="Category"
#     )

#     class Meta:
#         model = Product
#         fields = ['name', 'image', 'discount', 'description', 'category']


# class StaffForm(forms.ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['name', 'email', 'phone']