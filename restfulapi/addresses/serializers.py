from rest_framework import serializers
from .models import *


# class AddressSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Address
#         fields = ['name', 'phone_number', 'address', 'created']
#

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['userId', 'userPassword', 'userName', 'userAge', 'created']


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['userId','title', 'subTitle', 'content', 'createdDate', 'updatedDate']