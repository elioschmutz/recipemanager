from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    """
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipe_images')
    www = models.URLField()
    duration = models.IntegerField()
    portions = models.IntegerField()
    preparation = models.TextField()

    class Meta:
        permissions = (
            ('view_recipe', 'Can view recipe'),
        )

    def __str__(self):  # __unicode__ for Python 2
        return self.title
