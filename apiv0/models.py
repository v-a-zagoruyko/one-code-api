from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class ProductCollection(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class ProductColor(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='category')
    collection = models.ForeignKey(ProductCollection, on_delete=models.CASCADE, null=True, blank=True, related_name='collection')
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    color = models.ForeignKey(ProductColor, on_delete=models.CASCADE, null=True, blank=True, related_name='color')
    is_visible = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class ProductPhotos(models.Model):
    relation = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_photos')
    image = models.FileField()
