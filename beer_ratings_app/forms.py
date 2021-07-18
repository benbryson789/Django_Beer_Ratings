from django.forms import ModelForm
from beer_ratings_app.models import Beer, Review

class BeerForm(ModelForm):
    class Meta:
        model = Beer
        fields =  '__all__'

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__'