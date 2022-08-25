from django.http inport HttpResponse


def index(request):
	return HttpResponse('index')
