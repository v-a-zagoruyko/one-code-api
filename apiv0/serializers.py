from slugify import slugify
from rest_framework import serializers
from apiv0.models import *
from meta.models import *


class ProductCategoriesSerializer(serializers.ModelSerializer):
  slug = serializers.SerializerMethodField()

  def get_slug(self, obj):
    return slugify(obj.title, separator='_')

  class Meta:
    model = ProductCategory
    fields = ('id', 'title', 'description', 'slug')

class ProductFibersSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductFibers
    fields = ('title', 'description')

class ProductTypesSerializer(serializers.ModelSerializer):
  size = serializers.CharField(source='size.title')

  class Meta:
    model = ProductTypes
    fields = ('size', 'code', 'quantity')

class ProductPhotosSerializer(serializers.ModelSerializer):
  class Meta:
    model = ProductPhotos
    fields = ('image',)

class ProductSerializer(serializers.ModelSerializer):
  sizes = ProductTypesSerializer(source='product_types', many=True, read_only=True)
  fibers = ProductFibersSerializer(source='product_fibers', many=True, read_only=True)
  photos =  serializers.SerializerMethodField()
  slug =  serializers.SerializerMethodField()

  class Meta:
    model = Product
    fields = ('id', 'slug', 'title', 'description', 'price', 'sale_price', 'is_available', 'sizes', 'fibers', 'photos')

  def get_slug(self, obj):
    return '{}_{}'.format(slugify(obj.title, separator='_'), slugify(obj.description, separator='_'))
  
  def get_photos(self, obj):
    return list(map(lambda x: x.image.url, obj.product_photos.all()))

class ProductsByCategorySerializer(serializers.ModelSerializer):
  sizes = ProductTypesSerializer(source='product_types', many=True, read_only=True)
  fibers = ProductFibersSerializer(source='product_fibers', many=True, read_only=True)
  photos =  serializers.SerializerMethodField()
  slug =  serializers.SerializerMethodField()
  description =  serializers.SerializerMethodField()
  price =  serializers.SerializerMethodField()
  sale_price =  serializers.SerializerMethodField()
  is_available =  serializers.SerializerMethodField()

  class Meta:
    model = ProductCategory
    fields = ('id', 'slug', 'title', 'description', 'price', 'sale_price', 'is_available', 'sizes', 'fibers', 'photos')

  def get_is_available(self, obj):
    return obj.is_available

  def get_description(self, obj):
    return obj.description

  def get_price(self, obj):
    return obj.price

  def get_sale_price(self, obj):
    return obj.sale_price

  def get_slug(self, obj):
    return '{}_{}'.format(slugify(obj.title, separator='_'), slugify(obj.description, separator='_'))

  def get_photos(self, obj):
    return list(map(lambda x: x.image.url, obj.product_photos.all()))