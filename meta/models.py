from django.db import models


class Sizes(models.Model):
    title = models.CharField(max_length=8)

    def __str__(self):
        return self.title


class ProductTypes(models.Model):
    product = models.ForeignKey("apiv0.Product", on_delete=models.CASCADE, related_name='product_types')
    size = models.ForeignKey(Sizes, on_delete=models.CASCADE, related_name='size')
    code = models.CharField(max_length=128)
    quantity = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.product, self.size)

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class ProductFibers(models.Model):
    product = models.ForeignKey("apiv0.Product", on_delete=models.CASCADE, related_name='product_fibers')
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return ''

    class Meta:
        verbose_name = 'Состав и описание'
        verbose_name_plural = 'Состав и описание'