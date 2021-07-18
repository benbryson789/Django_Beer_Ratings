from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from beer_ratings_app.models import Beer, Review
from beer_ratings_app.forms import BeerForm, ReviewForm
from django.contrib.auth import authenticate,login
def index(request):
    if request.user.is_authenticated == False:
        return redirect("/signin")
    info = {
        "all_beers": Beer.objects.all()
    }
    return render(request, 'pages/beer/beer_list.html', info)
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
    return render(request,'pages/beer/signin.html')


def beer_detail(request, beer_id):
    try:
        beer = Beer.objects.get(id=beer_id)
    except:
        return HttpResponse(f"A beer with id {beer_id} doesn't exist")
    info = {
        'beer': beer
    }
    return render(request, 'pages/beer/beer_detail.html',info)

def review_list(request, beer_id):
    try:
        beer = Beer.objects.get(id=beer_id)
        info = { 'beer': beer}
        return render(request, 'pages/review/review_list.html',info)
    except:
        return HttpResponse(f"A beer with id {beer_id} doesn't exist")

def review_detail(request, beer_id, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except:
        return HttpResponse(f"A review with id {review_id} doesn't exist")
    info = {
        'review': review
    }
    return render(request, 'pages/review/review_detail.html',info)

def review_new(request, beer_id):
    form = ReviewForm()
    info = {'form': form }
    return render(request, 'pages/review/review_new.html', info)

def review_update(request):
    return render(request,'pages/review/update-reviews.html')