from django.contrib import admin

from .models import Recipe

from guardian.admin import GuardedModelAdmin


class RecipeAdmin(GuardedModelAdmin):
    """
    """


admin.site.register(Recipe, RecipeAdmin)
