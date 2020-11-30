from django.db import models
from django.utils import timezone


class ProductCategory(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.title


class ProductColor(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='category')
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=256)
    price = models.PositiveSmallIntegerField(default=0)
    sale_price = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
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


class Collection(models.Model):
    title = models.CharField(max_length=128)
    add_to_main_page = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)
    image = models.FileField(null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class Sale(models.Model):
    title = models.CharField(max_length=128)
    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    def is_started(self):
        if not self.time_start:
            return False
        if not self.time_end:
            return timezone.now() >= self.time_start
        return timezone.now() >= self.time_start and timezone.now() < self.time_end

    class Meta:
        verbose_name = 'Распродажа'
        verbose_name_plural = 'Распродажи'


class SaleProducts(models.Model):
    relation = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='sale_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sale_product')
    size = models.ForeignKey("meta.Sizes", on_delete=models.CASCADE, related_name='sale_size')
