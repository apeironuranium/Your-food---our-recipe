import datetime

from django.db import models
from django.utils import timezone


class Recipe(models.Model):
    recipe_text = models.CharField(max_length=400)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.recipe_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Food(models.Model):
    recipe = models.ForeignKey(Recipe)
    food_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.food_text


class Choice(models.Model):
    food = models.ForeignKey(Food)
    choice_text = models.CharField(max_length=200)

    def __str__(self):
        return self.choice_text
