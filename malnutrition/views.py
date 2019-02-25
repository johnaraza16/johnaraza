# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import list_route, api_view
from .models import AppUser, Food, Foodlog, Question
from .serializers import UserSerializer, FoodSerializer, FoodlogSerializer, QuestionSerializer, AppUserSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer

class FoodView(viewsets.ModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    
class FoodlogView(viewsets.ModelViewSet):
    queryset = Foodlog.objects.all()
    serializer_class = FoodlogSerializer

class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AlgoViewSet(viewsets.ViewSet):

    def list(self, request):
        """
        localhost:8000/algo/
        :param request:
        :return:
        """
        
        sample_dictionary = {
            "foodname": "sdfsdf"
        }

        return Response(sample_dictionary)


    @list_route(methods=["post", "get"], permission_classes=[], authentication_classes=[])
    def sample_post_request(self, request):
        """
        localhost:8000/algo/sample_post_request/

        SAMPLE FOR SAVING FOOD TO DATABASE

        {
            "calories": 23,
            "fats": 234,
            "foodname": "sdfsdf"
        }
        :return:
        """
        try:
            # request.data mao na siya a ng data na imong gi pasa sa database
            #import pdb; pdb.set_trace()
            data = request.data
            
            # for example mag save ka ug new food
            # mag initialize sa kag Food na model

            food = Food()
            food.calories= data['calories']
            food.fats= data['fats']
            food.foodname = data['foodname']
            food.save()

            return Response({"Successfully Saved. pwede ni mailisan ug basin unsa na gusto nimo i return"}, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

        
    @list_route(methods=["get"], permission_classes=[], authentication_classes=[])
    def sss(self, request):
        """
        localhost:8000/algo/sample_post_request/

        SAMPLE FOR SAVING FOOD TO DATABASE

        {
            "calories": 23,
            "fats": 234,
            "foodname": "sdfsdf"
        }
        :return:
        """
        try:
            oliver = {
                "a": "jfdshkjdhfksdf",
                "b": "sdkfjsdlkfjlsd",
                "c": "kfdsljlfkjsdlfs"
            }
            return Response(oliver, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

        
    @list_route(methods=["post", "get"], permission_classes=[], authentication_classes=[])
    def get_user(self, request):
        """
        localhost:8000/test/algo/get_user/

        GETTING CURRENT LOGGED IN USER

        {
            "username": "fosdjrklsdjfkls",
        }
        :return:w
        """
        try:
            data = request.data
            user = User.objects.get(username = data['username'])
            app_user = AppUser.objects.get(user=user)
            serializer = AppUserSerializer(app_user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)

    @list_route(methods=["get"], permission_classes=[], authentication_classes=[])
    def get_food(self, request):
        """
        localhost:8000/test/algo/get_food/

        GETTING THREE RANDOMIZED FOOD
        
        """
        try:
            get_food = Food.objects.all().order_by("?")[:3]
            serializer = FoodSerializer(get_food, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_400_BAD_REQUEST)