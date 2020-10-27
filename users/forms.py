from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Order, Product
from django.contrib.auth.models import User

class OrderUpdate(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""  # Removes : as label suffix
		

	class Meta:
		model = Order
		fields = "__all__"

		widgets = {
			'customer': forms.Select(attrs={'class':'form-control  bg-light text-info'}),
			'product': forms.Select(attrs={'class':'form-control bg-light text-info'}),
			'status': forms.Select(attrs={'class':'form-control bg-light text-info'}),
			'tags': forms.SelectMultiple(attrs={'class':'form-control bg-light text-info'}),
		}



class NewProducts(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""  # Removes : as label suffix
		

	class Meta:
		model = Product
		fields = "__all__"

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control  bg-light text-info'}),
			'description': forms.TextInput(attrs={'class':'form-control bg-light text-info'}),
			'price': forms.TextInput(attrs={'class':'form-control bg-light text-info'}),
			'category': forms.Select(attrs={'class':'form-control bg-light text-info'}),
		}


class CreateUserForm(UserCreationForm):

	password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control bg-light text-info'}),
    )
	password2 = forms.CharField(
		label="Confirm password",
    	widget=forms.PasswordInput(attrs={'class':'form-control bg-light text-info'}),
    )


	class Meta:
		model = User
		fields = ['username','email','password1','password2']

		widgets = {
			'username': forms.TextInput(attrs={'class':'form-control  bg-light text-info'}),
			'email': forms.EmailInput(attrs={'class':'form-control bg-light text-info'}),
		}
