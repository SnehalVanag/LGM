from django import forms
from .models import Franchise

class FranchiseForm(forms.ModelForm):
    class Meta:
        model = Franchise
        fields = ['name', 'address', 'contact_email']