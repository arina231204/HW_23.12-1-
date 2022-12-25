from rest_framework import serializers

from .models import Product,Category, Company


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

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


