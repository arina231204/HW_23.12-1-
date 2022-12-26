import json

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Category,Company, Product
from rest_framework import generics, status
from .serializers import  ProductSerializer,CompanySerializer,CategorySerializer
from rest_framework import viewsets




@api_view(['POST', 'GET'])
def create_product(request):
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(instance=product, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT','DELETE'])
def detail_product(request, pk):
    product = generics.get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        serializer = ProductSerializer(instance=product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP)

    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






@api_view(['POST','GET'])
def create_company(request):
    if request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    if request.method == 'GET':
        company = Company.objects.all()
        serializer = CompanySerializer(instance=company, many=True )
        return Response(serializer.data, status=status.HTTP_200_OK)




@api_view(['GET', 'PUT','DELETE'])
def detail_company(request,pk):
    company = generics.get_object_or_404(Company, pk=pk)
    if request.method == 'GET':
        serialize = CompanySerializer(instance=company)
        return Response(serialize.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST','GET'])
def create_category(request):
    if request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySerializer(instance=category, many=True )
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_category(request,pk):
    category = generics.get_object_or_404(Category, pk=pk)
    if request.method == 'GET':
        serialize = CategorySerializer(instance=category)
        return Response(serialize.data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)























# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
# class CompanyCreateListView(generics.ListCreateAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer
#
# class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Company.objects.all()
#     serializer_class = CompanySerializer

# @csrf_exempt
# def create_category(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         new_category = Category.objects.create(**data)
#         json_data = {
#             "name":new_category.name,
#         }
#         print(new_category)
#         return HttpResponse("OK")
#     if request.method == 'GET':
#         categories = Category.objects.all()
#         data = []
#         for category in categories:
#             data.append(
#                 {
#                     "name":category.name,
#                 }
#             )
#         json_data = json.dumps(data)
#         return JsonResponse(json_data, safe=False)

# class CategoryViewSet(viewsets.ModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

