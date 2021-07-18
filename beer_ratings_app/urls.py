from django.urls import path
from beer_ratings_app import views


urlpatterns = [

    path('', views.index, name='home'),
    path('signin/', views.signin, name='signin'),
    path('<int:beer_id>', views.beer_detail, name='beer_detail'),
    path('<int:beer_id>/reviews',views.review_list, name='review_list'),
    path('<int:beer_id>/reviews/new',views.review_new, name='review_new'),
    path('<int:beer_id>/reviews/<int:review_id>/update',views.review_update, name='review_update'),
    path('<int:beer_id>/reviews/<int:review_id>',views.review_detail, name='review_detail'),
    
]