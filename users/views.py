from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
	# fetch data from customer table
	customer = Customer.objects.all()
	# fetch data from orders table
	order = Order.objects.all()
	# total number of customers
	tcx = customer.count()
	# total number of orders
	tord = order.count()
	# pending orders
	pod = order.filter(status='Pending').count()
	# delivered orders
	dod = order.filter(status='Delivered').count()
	# shipped orders
	sod = order.filter(status='Shipped').count()

	context = {'customer': customer, 'order': order,'tcx':tcx ,'pod':pod,'sod':sod,'dod':dod,'tord':tord}
	return render( request, 'dashboard.html', context)

def user(request, pk):
	# fetch data from customer table
	users = Customer.objects.get(id=pk)
	# fetch data from orders table
	order = users.order_set.all()

	tod = order.count()

	context = {'users':users, 'order':order, 'tod' : tod}

	return render( request, 'users.html', context)

def createOrder(request):
	form = OrderUpdate()

	if request.method == 'POST':
		form = OrderUpdate(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {"form" : form }

	return render(request, 'create_order.html', context)



def updateOrder(request, pk):
	order = Order.objects.get(id=pk)

	form = OrderUpdate(instance=order)

	if request.method == 'POST':
		form = OrderUpdate(request.POST, instance=order)
		if form.is_valid():
			form.save()
		return redirect('/')	

	context = {'form':form}

	return render(request, 'update_order.html', context )

def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)

	form = OrderUpdate(instance=order)

	if request.method == 'POST':
		order.delete()
		return redirect('/')	

	context = {'form':form}

	return render(request, 'delete_order.html', context )




def orders(request):
	# fetch data from orders table
	order = Order.objects.all()

	return render( request, 'orders.html', {'order': order})

def products(request):

	products = Product.objects.all()

	context = {"products" :products}

	return render (request, 'products.html', context)



def newProducts(request):
	form = NewProducts()

	if request.method == 'POST':
		form = NewProducts(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {"form" : form }

	return render(request, 'create_product.html', context)