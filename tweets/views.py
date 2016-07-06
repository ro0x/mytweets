from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from tweets.models import User
from tweets.models import Tweet

# Create your views here.


class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Rick O"
        return render(request, 'base.html', params)

    def post(self, request):
        return HttpResponse('I am called from a POST request')

class Profile(View):
    """
    User profile page reachable from /user/<username>URL
    """
    def get(self, request, username):
        params = {}
        user = User.objects.get(username=username)
        tweets = Tweet.objects.filter(user=user)
        params["tweets"] = tweets
        params["user"] = user
        return render(request, 'profile.html', params)
