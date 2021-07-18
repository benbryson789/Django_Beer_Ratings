from django.contrib import admin

from beer_ratings_app.models import Beer, Review

admin.site.register(Beer)
admin.site.register(Review)