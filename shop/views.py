from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category, Product
from .serializers import ProductSerializer


class CustomLoginView(LoginView):
    template_name = 'shop/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('recent_products')


class RegisterView(FormView):
    template_name = 'shop/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('recent_products')

    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    # prevent authenticated users from accessing registerview
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('recent_products')
        return super(RegisterView, self).get(*args, **kwargs)


class RecentProductsView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'shop/recent_products.html'
    context_object_name = 'recent_products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RecentProductsView, self).get_context_data(**kwargs)
        context['recent_products'] = Product.objects.order_by('date_added')[:5]
        return context


class CategoriesView(ListView):
    model = Category
    template_name = 'shop/categories.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductsView(ListView):
    model = Product
    template_name = 'shop/products.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/product_details.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['product'] = Product.objects.get(pk=self.kwargs['pk'])
        context['formatted_price'] = '{:,.2f}'.format(context['product'].price)
        return context


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_details.html'
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.get(pk=self.kwargs['pk'])
        context['products'] = Product.objects.filter(category=context['category'])
        return context


class SearchView(ListView):
    model = Product
    template_name = 'shop/search.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(
            Q(name__icontains=self.request.GET['q']) |
            Q(description__icontains=self.request.GET['q']) |
            Q(category__name__icontains=self.request.GET['q'])
        )
        return context
