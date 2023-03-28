from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    ingredients = models.CharField(max_length=200)
    customs_ingredients = models.CharField(max_length=200)
    gpt3_response = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.ingredients} - {self.customs_ingredients}"