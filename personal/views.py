from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/basic.html', {'content':['If your would like to contact me, here is my email...', 'labusby1@gmail.com']})