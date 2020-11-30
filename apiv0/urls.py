from django.conf.urls import url, include
from rest_framework import routers

from apiv0.views import *

router = routers.DefaultRouter()
router.register(r'product-categories', ProductCategoriesViewSet)
router.register(r'product', ProductViewSet, basename='Product')
router.register(r'products-by-category', ProductsByCategoryViewSet, basename='Products')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
]