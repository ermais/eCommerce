from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class ProductQueryset(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

class Product(models.Manager):
	def get_queryset(self):
		return ProductQueryset(self.model,using=self._db)
	
	def all(self,*args,**kwargs):
		return self.get_queryset().active()
	
class Product(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank=True,null=True)
	pub_date = models.DateTimeField(auto_now_add=True,auto_now=False)
	inventory = models.PositiveIntegerField(default=1)
	price = models.PositiveIntegerField()
	sale_price = models.PositiveIntegerField()
	active = models.BooleanField(default=True)
	
	def __str__(self):
		return  self.title
	
	def get_price(self):
		if self.sale_price is None:
			return self.sale_price
		else:
			return self.price
	

class Specification(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	title = models.CharField(max_length=120)
	description = models.CharField(max_length=250)
	
	def __str__(self):
		return self.title
	


def image_upload_to(instance, filename):
	title = instance.product.title
	slug = slugify(title)
	basename, file_extension = filename.split(".")
	new_filename = "%s-%s.%s" % (slug, instance.id, file_extension)
	return "products/%s/%s" % (slug, new_filename)


class ProductImage(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	image = models.ImageField(upload_to=image_upload_to)
	
	def __str__(self):
		return self.product.title
	
	

