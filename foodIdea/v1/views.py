from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


from MealPlanner.utils import create_meal
from MealPlanner.models import Recipe
from .serializer import RecipeSerializer, UserSerializer



class RecipeMakerViewSet(ModelViewSet):
    """ In this view set we create a new recipe 
        with the ingredients and custom ingredients
        recived from the frontend """
    
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    
    def create(self, request):
        if request.data.get('ingredientes') is None:
            return Response({'error': 'No ingredients were provided'})
        
        respose_from_gpt = create_meal(request.data.get('ingredientes'), request.data.get('custom_ingredients'))
        request.data.mutable = True
        request.data['gpt3_response'] = respose_from_gpt
        request.data.mutable = False

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'recipe': respose_from_gpt['choices'][0]['message'].content})

class CreateUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request):
        if request.data.get('username') is None:
            return Response({'error': 'No username was provided'})
        if request.data.get('password') is None:
            return Response({'error': 'No password was provided'})
        if request.data.get('email') is None:
            return Response({'error': 'No email was provided'})
        if request.data.get('is_superuser') is not None or request.data.get('is_staff') is not None or request.data.get('user_permissions') is not None or request.data.get('groups') is not None:
            return Response({'error': 'You are not allowed'})
        
        user = User.objects.filter(username=request.data.get('username'))
        if user:
            return Response({'error': 'Username already exists'})
        user = User.objects.filter(email=request.data.get('email'))
        if user:
            return Response({'error': 'Email already exists'})
        
        user = User.objects.create_user(
            username=request.data.get('username'),
            password=request.data.get('password'),
            email=request.data.get('email'),
        )
        user.save()
        return Response({'message': 'User created successfully'})