from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()
