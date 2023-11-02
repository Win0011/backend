from django.db import models

class product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="product_images")
    category = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)

    class meta:
        verbose_name_plural = "Product"

    def __str__(self):
        return self.name
