from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from . models import *
from . serializers import * 
# Create your views here.

class CUDTestModelAPI(APIView):
    '''For Get, Create, Update, Delete of events '''

    def post(self, request, *args, **kwargs):
        ''''post method to create new TestModel'''
        name = request.data.get("name")
        age = request.data.get("age")
        email = request.data.get("email")

        testModel = User.objects.create(
            name  = name,
            age= age,
            email= email
        )

        serializer = UserSerializer(testModel, many=False)
        return Response({
            "testModel": serializer.data
        },status=status.HTTP_201_CREATED)
    

    def put(self, request, *args, **kwargs):
        '''put method to update TestModels'''
        id = request.data.get("id")
        testModel = User.objects.filter(id=id).first() #noqa
        name = request.data.get("name")
        email = request.data.get("email")
        age = request.data.get("age")

        if testModel:
            testModel.name =name
            testModel.age = age
            testModel.email = email
            testModel.save()
            serializer = UserSerializer(testModel, many=False)
            return Response({
                "testModel":serializer.data
            },status=status.HTTP_200_OK)
        else:
            return Response({
                "message":"Event Not Found"
            }, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, *args, **kwargs):
        '''delte method to delete TestModels'''
        id = request.data.get("id")
        testModel = User.objects.filter(id=id).first() #noqa
        
        if testModel:
            testModel.delete()
            return Response({
                "message":'testModel deleted successfully'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                "message": "testModel Not Found"
            }, status=status.HTTP_404_NOT_FOUND)

        

    def get(self, request, *args, **kwargs):
        '''uses get method to fetch all created testModels'''
        testModels = TestModel.objects.all().order_by('-id')
        serializer = TestModelSerializer(testModels, many=True)
        return Response({
            "testModels": serializer.data
        },status=status.HTTP_200_OK)
        
    