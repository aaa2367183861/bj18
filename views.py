from django.http inport HttpResponse
from django.shortcuts import redirects

def index(request):
	return HttpResponse('index')

def login(request):
	return redirect("/index")
