from django.shortcuts import render
from django.db.models import Q

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Product, ProductImage, Specification



class ProductListView(LoginRequiredMixin,ListView):
	model = Product
	template_name = 'products/product_list.html'
	
	def get_queryset(self,*args,**kwargs):
		qs = super(ProductListView, self).get_queryset(*args,**kwargs)
		query = self.request.GET.get("item")
		if query:
			qs = self.model.objects.filter(
				Q(title__contains=query) |
				Q(description__contains=query)
			)
		return qs
	
	
class ProductDetailView(DetailView):
	model = Product
	context_object_name = 'product'
	template_name = 'products/product_detail.html'
