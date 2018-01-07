from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    """
    """
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creator")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    creation_date = models.DateField(auto_now_add=True, blank=True)
    modification_date = models.DateField(auto_now=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipe_images', blank=True)
    www = models.URLField(blank=True)
    duration = models.IntegerField(blank=True, null=True)
    portions = models.IntegerField(blank=True, null=True)
    preparation = models.TextField(blank=True)

    class Meta:
        permissions = (
            ('view_recipe', 'Can view recipe'),
        )

    def __str__(self):  # __unicode__ for Python 2
        return self.title
