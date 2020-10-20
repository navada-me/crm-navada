from django.urls import path
from . import views 

urlpatterns = [
	path('',views.home, name="home"),
	path('users/<str:pk>/',views.user , name="user"),
	path('orders/',views.orders , name="orders"),
	path('products/',views.products , name="products"),
	path('newProducts/',views.newProducts , name="newProduct"),
	path('createOrder/',views.createOrder , name="createOrder"),
	path('updateOrder/<str:pk>/',views.updateOrder , name="updateOrder"),
	path('deleteOrder/<str:pk>/',views.deleteOrder , name="deleteOrder"),
]