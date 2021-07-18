from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


class Beer(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    abv = models.DecimalField(decimal_places=2, max_digits=3)
    style = models.CharField(max_length=64)

    def __str__(self):
        return  f"BEER:  {self.name}"

class Review(models.Model):
    content = models.TextField()
    beer = models.ForeignKey(Beer, related_name="reviews", on_delete=models.CASCADE)
    reviewer = models.ForeignKey(User,  related_name="reviews",on_delete=models.CASCADE)
    
    class Rating(models.IntegerChoices):
            TERRIBLE = 1
            DECENT = 2
            OKAY = 3
            GOOD = 4
            EXCELLENT = 5

    rating = models.IntegerField(choices=Rating.choices)

    def __str__(self):
        return f"REVIEW: {self.content} for {self.beer}"
