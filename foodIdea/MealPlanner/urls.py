from django.urls import path
from .views import MealPlannerView, MealMakerView

urlpatterns = [
    path("", MealPlannerView.as_view(), name="meal_planner"),
    path("yourplate/", MealMakerView.as_view(), name="meal_maker"),
]
