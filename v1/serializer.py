from django.contrib.auth.models import User
from rest_framework import serializers
from drf_spectacular.utils import extend_schema_field

from MealPlanner.models import Recipe
from MealPlanner.utils import create_meal

class RecipeSerializer(serializers.ModelSerializer):

    gpt3_response = serializers.SerializerMethodField(required=False, read_only=True)
    recipe = serializers.SerializerMethodField(required=False, read_only=True)
    
    class Meta:
        model = Recipe
        fields = (
            'ingredients',
            'customs_ingredients',
            'title',
            'recipe',
            'is_saved',
            'user',
            'gpt3_response',
        )

    @extend_schema_field(serializers.JSONField())
    def get_gpt3_response(self, obj):
        return create_meal(obj.ingredients, obj.customs_ingredients)
    
    @extend_schema_field(serializers.CharField())
    def get_recipe(self, obj):
        return obj.gpt3_response["choices"][0]["message"].content

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password'
        )
