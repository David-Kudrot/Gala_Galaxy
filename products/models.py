from django.db import models

# Create your models here.
class CategoryModel(models.Model):
    name=models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name
    
    
class ProductModel(models.Model):
    name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to="products/images")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    