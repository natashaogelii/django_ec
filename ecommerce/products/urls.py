from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.home, name="home"),
    path('add_category/', views.add_category, name="add_category"),
    path('category_list/', views.category_list, name="category_list"),
    path("add/", views.add_product, name="add_product"),
    path("products_list/", views.product_list, name="products_list"),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),

]
