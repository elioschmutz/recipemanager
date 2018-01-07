from .models import Recipe
from rest_framework import serializers
from recipemanager.users.serializers import UserSerializer


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    creator = serializers.CreateOnlyDefault(serializers.CurrentUserDefault())
    owner = serializers.CreateOnlyDefault(serializers.CurrentUserDefault())
    image = serializers.ImageField(max_length=None, required=False,
                                   allow_empty_file=True, use_url=True)

    class Meta:
        model = Recipe
        fields = '__all__'
