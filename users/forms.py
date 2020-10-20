
from django import forms
from .models import Order, Product

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