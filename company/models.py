from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=225)
    price = models.IntegerField()
    company = models.CharField(max_length=225)
    category = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name






