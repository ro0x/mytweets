from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render

class Index(View):
    def get(self, request):
        params = {}
        params["name"] = "Rick O"
        return render(request, 'base.html', params)
    def post(self, request):
        return HttpResponse('I am called from a POST request')

# Create your views here.
