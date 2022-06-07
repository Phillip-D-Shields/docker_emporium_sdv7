from django.urls import path
from . import views

urlpatterns = [
    # gets
    path('', views.get_routes),
    path('categories/', views.get_categories),
    path('category/<int:category_id>/', views.get_category_by_id),
    path('category/<str:category_name>/', views.get_category_by_name),
    path('products/', views.get_products),
    path('product/<int:product_id>/', views.get_product_by_id),
    path('product/<str:product_name>/', views.get_product_by_name),
    # posts
    path('new_product/', views.new_product),
    # puts
    path('update_product/<int:product_id>/', views.update_product),
    # deletes
    path('delete_product/<int:product_id>/', views.delete_product),
]
