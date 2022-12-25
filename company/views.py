import json

from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Category,Company, Product
from rest_framework import generics
from .serializers import  ProductSerializer,CompanySerializer,CategorySerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CompanyCreateListView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

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

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

