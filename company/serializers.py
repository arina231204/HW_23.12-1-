from rest_framework import serializers

from .models import Product,Category, Company


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=225)
    price = serializers.IntegerField()
    company_id = serializers.IntegerField()
    category_id = serializers.IntegerField()



    def create(self, validated_data):
        product = Product.objects.create(
            name = validated_data['name'],
            price = validated_data['price'],
            company_id = validated_data['company_id'],
            category_id = validated_data['category_id'],
        )
        return product

    def update(self, instance,validated_data):
        instance.name = validated_data['name']
        instance.price = validated_data['price']
        instance.company_id = validated_data['company_id']
        instance.category_id = validated_data['category_id']
        return instance



class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=225)
    address = serializers.CharField(max_length=225)




    def create(self, validated_data):
        company = Company.objects.create(
            name = validated_data['name'],
            address = validated_data['address'],
        )
        return company

    def update(self, instance,validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        return instance


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=225)




    def create(self, validated_data):
        category = Category.objects.create(
            name = validated_data['name'],
        )
        return category

    def update(self, instance,validated_data):
        instance.name = validated_data['name']
        return instance


