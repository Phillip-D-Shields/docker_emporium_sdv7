from django.urls import path
from .views import CustomLoginView, RegisterView, RecentProductsView, CategoriesView, ProductsView, ProductDetailView, CategoryDetailView, SearchView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('products/search/', SearchView.as_view(), name='search'),
    path('', RecentProductsView.as_view(), name='recent_products'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('products/', ProductsView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category'),
]
