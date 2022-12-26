from django.db import models



class Company(models.Model):
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name






