from decimal import Decimal
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save, post_save

from products.models import Product

class CartItem(models.Model):
	cart = models.ForeignKey('Cart',on_delete=models.CASCADE)
	item = models.ForeignKey(Product,on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=1)
	line_item_total = models.DecimalField(max_digits=12,decimal_places=2)
	
	def __str__(self):
		return self.item.title
	def remove(self):
		return "%s?item=%s&delete=True" % (reverse('cart_view'),self.item.id)
	
def cart_item_reciver(sender,instance,*args,**kwargs):
	qty = instance.quantity
	if qty >= 1:
		price = instance.item.get_price()
		line_item_total = Decimal(qty)*Decimal(price)
		instance.line_item_total = line_item_total

pre_save.connect(cart_item_reciver,sender=CartItem)
def car_item_post_save(sender,instance,*args,**kwargs):
	instance.cart.update_total()
post_save.connect(car_item_post_save,sender=CartItem)

class Cart(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,null=True,blank=True)
	items = models.ManyToManyField(Product, through=CartItem)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	sub_total = models.DecimalField(max_digits=12,decimal_places=2)
	
	def update_total(self):
		subtotal = 0
		items = self.cartitem_set.all()
		for item in items:
			subtotal += item.line_item_total
		self.sub_total = subtotal
		self.save()
	
	def __str__(self):
		return str(self.id)
	