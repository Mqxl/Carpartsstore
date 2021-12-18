from django import forms

from django.forms import ModelForm
from django.forms.widgets import EmailInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from django import forms
from django.core.files.images import get_image_dimensions

from orders.models import OrderItem


 



class SignUpForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=30, required=False, help_text='First name.',)
    last_name = forms.CharField(max_length=30, required=False, help_text='Last name.')
    email = forms.EmailField(max_length=254, help_text='Email')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



 

 
 
# creating a form
class OrderForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = OrderItem
 
        # specify fields to be used
        fields = [
            "order",
            "product",
            "price",
            "quantity",
        ]



