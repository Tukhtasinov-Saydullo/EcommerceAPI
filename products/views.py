from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product, Category
from .serializers import ProductListSerializer, CategoryListSerializer


# Create your views here.

@api_view(['GET'])
def get_products_list(request):
    products = Product.objects.order_by("-id")
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_category_list(request):
    category = Category.objects.order_by("-id")
    serializer = CategoryListSerializer(category, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductListSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def get_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategoryListSerializer(category)
    return Response(serializer.data)
