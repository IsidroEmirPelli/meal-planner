from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from MealPlanner.constants import OPENAI_API_KEY
from MealPlanner.utils import create_meal
from MealPlanner.models import Recipe
from .serializer import RecipeSerializer, UserSerializer


class RecipeMakerViewSet(ModelViewSet):
    """In this view set we create a new recipe
    with the ingredients and custom ingredients
    recived from the frontend"""
    
    serializer_class = RecipeSerializer
    
    def list(self,request):
        queryset = self.get_queryset()
        queryset = queryset.filter(user=request.user)
        serializer = RecipeSerializer(queryset, many=True)
        return Response({"recipes": serializer.data})
    
    def partial_update(self, request, pk=None):
        recipe = get_object_or_404(Recipe, pk=pk)
        recipe.is_saved = request.data.get('is_saved', recipe.is_saved)
        recipe.save()
        serializer = self.get_serializer(recipe)
        return Response(serializer.data)
    
class CreateUserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
