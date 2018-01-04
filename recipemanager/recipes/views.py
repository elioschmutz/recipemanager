from .models import Recipe
from .serializers import RecipeSerializer
from guardian.shortcuts import get_objects_for_user
from rest_framework import permissions
from rest_framework import viewsets


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited.
    """
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.all()

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        return get_objects_for_user(self.request.user, 'recipes.view_recipe')
