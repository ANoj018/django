from django.db import models


# Create your models here.
# class Users(models.Model):
#     full_name = models.CharField(max_length=100)
#     email = models.EmailField(unique= True)
#     password = models.CharField(max_length=100)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     address = models.TextField(blank=True, null=True)
#     birth_date = models.DateTimeField(auto_now= True)

# class Product(models.Model):
#     STATUS = [
#         ('P', "pending"),
#         ('C',"Completed"),
#         ('F',"Failed"),
#     ]
#     name = models.CharField(max_length=100)
#     slug = models.SlugField(unique=True)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inverntory = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True )
#     status = models.CharField(max_length=1, choices=STATUS, default='p')


# class Student:
#     def init(self, name, age, height):
#         self.name = name
#         self.age = age
#         self.height = height
#     def greet(self):
#         print("hellp welcome to this class. my name is {self.name} amd i am {self.age} years old")


# Student1 = Student("anu",20,6)
# Student1.greet()
