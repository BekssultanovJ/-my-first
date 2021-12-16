from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug= models.SlugFiled(max_length=50, primary_key=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='products')

    image = models.ImageField(upload_to='products', null=True, blank=True)

    def __str__(self):
        return  self.name

#TODO: реализовать возмозность хранить несколько изображений
class ProductImage(models.Model):
    pass

#варианты on_delete
#CASCADE - при удалении котегории, удаляются соответсвующие ей продукты
#RESTRICT -
# PROTECT -запрещает удление котегории, если есть связанные с ней продукты
# SET_NULL - при удалении котегории у продуктов котигории стоновится  NULL
# SET_DEFAULT - при удалении котегорииб продуктам присваевается дефолтная категория