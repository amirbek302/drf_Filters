from rest_framework import generics

from .models import Meal, Category, Area
from .serializers import MealListSerializer, MealDetailSerializer, CategorySerializer, AreaSerializer


# Create your views here.

class MealAPI(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealListSerializer

class MealDetailsAPI(generics.ListAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealDetailSerializer

class CategoryAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AreaAPI(generics.ListAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer