from rest_framework import serializers
from rest_framework.response import Response

from . models import *

class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = '__all__'



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ('name', 'age', 'email', 'role')
        extra_kwargs = {'password':{'write_only': True}}

    
    def create(self, validated_data):
        user = TestModel.objects.create_user(
            email= validated_data['email'],
            password= validated_data['password'],
            name= validated_data['name'],
            age = validated_data['age'],
            role = validated_data['role'],
        )
        return user