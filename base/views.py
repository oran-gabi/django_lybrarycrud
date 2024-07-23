from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from base.serializers import ProductSerializer
from .models import Product

# Register endpoint
@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    first_name = request.data.get('first_name', '')
    last_name = request.data.get('last_name', '')

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email,
        first_name=first_name,
        last_name=last_name,
        is_staff=False,
        is_active=True,
        is_superuser=False
    )
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

# Index endpoint
@api_view(['GET'])
def index(req):
    return Response('hello')

# Test endpoint
@api_view(['GET'])
def test(req):
    return Response({'test': 'success'})

# Member-only endpoint
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def member(req):
    return Response({'member': 'only'})

# Public endpoint
@api_view(['GET'])
def allpub(req):
    return Response({'test': 'public'})



# Product management endpoint
@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def product(request, id=None):
    if request.method == 'GET':
        if id is not None:
            product = get_object_or_404(Product, pk=id)
            return Response(ProductSerializer(product).data)
        else:
            products = Product.objects.all()
            return Response(ProductSerializer(products, many=True).data)

    elif request.method == 'POST':
        prod_serializer = ProductSerializer(data=request.data)
        if prod_serializer.is_valid():
            prod_serializer.save()
            return Response({'message': 'Product created successfully'}, status=status.HTTP_201_CREATED)
        return Response(prod_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    elif request.method in ['PUT', 'PATCH']:
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        
        prod_serializer = ProductSerializer(product, data=request.data, partial=(request.method == 'PATCH'))
        if prod_serializer.is_valid():
            prod_serializer.save()
            return Response({'message': 'Product updated successfully'}, status=status.HTTP_200_OK)
        return Response(prod_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
