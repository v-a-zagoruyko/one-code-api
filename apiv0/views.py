from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from apiv0.models import *
from apiv0.serializers import *
from apiv0.permissions import *


class ProductCategoriesViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny, )
    queryset = ProductCategory.objects.filter(category__isnull=False).distinct()

    def get_serializer_class(self):
        return ProductCategoriesSerializer

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Product.objects.all()

    def get_serializer_class(self):
        return ProductSerializer

class ProductsByCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    queryset = Product.objects.filter(is_visible=True)
    
    def list(self, request, *args, **kwargs):
        queryset = []

        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            queryset = Product.objects.filter(category=category_id, is_visible=True)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        return ProductsByCategorySerializer
