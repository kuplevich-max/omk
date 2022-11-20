from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    title = models.CharField(max_length=100)
    class Meta:
        verbose_name='Категория'
        verbose_name_plural = 'Категории'
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=2000)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title