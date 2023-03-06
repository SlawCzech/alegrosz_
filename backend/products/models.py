from django.db import models

from products.validators import validate_file_type


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    stock_count = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-price', )
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

class Picture(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    image = models.FileField(upload_to='images/', validators=[validate_file_type])

    def __str__(self):
        return self.image.name
