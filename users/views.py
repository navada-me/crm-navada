from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages


# Create your views here.
@csrf_protect
def registerUser(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()


		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')

		context = {'form': form}
		return render(request, 'register.html', context)

@csrf_protect
def loginUser(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username or Password is incorrect')


		context = {}
		return render(request, 'login.html', context)	


def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
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

@login_required(login_url='login')
def user(request, pk):
	# fetch data from customer table
	users = Customer.objects.get(id=pk)
	# fetch data from orders table
	order = users.order_set.all()

	tod = order.count()

	context = {'users':users, 'order':order, 'tod' : tod}

	return render( request, 'users.html', context)

@login_required(login_url='login')
def createOrder(request):
	form = OrderUpdate()

	if request.method == 'POST':
		form = OrderUpdate(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {"form" : form }

	return render(request, 'create_order.html', context)


@login_required(login_url='login')
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

@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)

	form = OrderUpdate(instance=order)

	if request.method == 'POST':
		order.delete()
		return redirect('/')	

	context = {'form':form}

	return render(request, 'delete_order.html', context )



@login_required(login_url='login')
def orders(request):
	# fetch data from orders table
	order = Order.objects.all()

	return render( request, 'orders.html', {'order': order})

@login_required(login_url='login')
def products(request):

	products = Product.objects.all()

	context = {"products" :products}

	return render (request, 'products.html', context)


@login_required(login_url='login')
def newProducts(request):
	form = NewProducts()

	if request.method == 'POST':
		form = NewProducts(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {"form" : form }

	return render(request, 'create_product.html', context)