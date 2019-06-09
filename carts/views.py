from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.views import View
from django.views.generic.detail import SingleObjectMixin

from .models import Cart, CartItem
from products.models import Product

class CartView(SingleObjectMixin,View):
	model = Cart
	
	def get_object(self,*args,**kwargs):
		cart_id = self.request.session.get("cart")
		if cart_id == None:
			cart = Cart()
			cart.save()
			cart_id = cart.id
			self.request.session["cart"] = cart_id
		cart = self.model.objects.get(id=cart_id)
		# if self.request.user.is_authenticated():
		# 	cart.user = self.request.user
		# 	cart.save()
		# cart = self.model.objects.get(id=cart_id)
		return cart
	
	
	def get(self,request,*args,**kwargs):
		cart = self.get_object()
		if request.is_ajax():
			print(request.GET.get("item"))
			return JsonResponse({"success":True})
			
		item_id = request.GET.get("item")
		qty = request.GET.get("qty",1)
		item_delete = request.GET.get("delete",False)
		if item_id:
			item = get_object_or_404(Product,id=item_id)
			try:
				if int(qty) < 1:
					item_delete = True
			except:
				raise Http404
			cart_item = CartItem.objects.get_or_create(item=item,cart=cart)[0]
			if item_delete:
				cart_item.delete()
			else:
				cart_item.quantity = int(qty)
				cart_item.save()
			
			
		return render(request,'carts/view.html',{"object":self.get_object()})
		