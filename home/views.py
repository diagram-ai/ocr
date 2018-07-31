from django.shortcuts import render

def index(request):
	return render(request, 'home/upload.html')
	#render looks in the templates directory
	#if you have multiple apps, create another directory for the app
	#in templates directory to avoid conflicting names
