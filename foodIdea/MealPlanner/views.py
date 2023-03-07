from django.shortcuts import render
from django.views import View
from .utils import create_meal

# Create your views here.


class MealPlannerView(View):
    def get(self, request):
        return render(request, 'index.html')

class MealMakerView(View):
    """ Here we recive requests with the ingredients for 1 person
        We then return a food with that ingredients"""
    def post(self, request):
        ingredientes = request.POST.get('ingredientes')
        menu = create_meal(ingredientes)
        context = {
            'menu': menu.content
        }

        return render(request, 'yourplate.html', context)

    