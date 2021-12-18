from django import forms
from django.forms.widgets import HiddenInput, TextInput
from django.http import request
from .models import Order


class OrderCreateForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city','userid']
        widgets = {
            'userid': forms.TextInput(attrs={'type': 'hidden'}),
        }
    def __init__(self, *args, **kwargs):
        super(OrderCreateForm, self).__init__(*args, **kwargs)
        self.fields['userid'].required = False
        
        

    
        