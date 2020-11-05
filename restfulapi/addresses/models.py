from django.db import models

# Create your models here.


# class Address(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
#     name = models.CharField(max_length=10)
#     phone_number = models.CharField(max_length=13)
#     address = models.TextField()
#
#     class Meta:
#         ordering = ['created']


class User(models.Model):
    userId = models.CharField(max_length=20)
    userPassword = models.CharField(max_length=20)
    userName = models.CharField(max_length=10)
    userAge = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Board(models.Model):
    userId = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    subTitle = models.CharField(max_length=50)
    content = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['createdDate']
