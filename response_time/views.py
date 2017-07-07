from django.shortcuts import render
from django.shortcuts import get_object_or_404
from root import *
from rt import run_response
from long_convo import run_long

# Create your views here.

def root(request):
	return render(request, 'response_time/src/root.html', {})

def response_time(request):
	if request.method =="GET":
		return render(request, "response_time/src/response_time.html",{})

	elif request.method == "POST":
		try:
			crawl = int(request.POST.get("crawl"))
		except:
			pass
		crawl_dict = run_response(crawl)

		return render(request, "response_time/src/response_time.html",{
				"crawl_list" : crawl_dict.items(),
			})


def start_hour(request):
	return render(request, 'response_time/src/start_hour.html', {})

def long_convo(request):
	if request.method =="GET":
		return render(request, 'response_time/src/long_convo.html', {})

	if request.method == "POST":
		crawl = int(request.POST.get("crawl"))
		view = int(request.POST.get("view"))	
		text = run_long(crawl, view)

		return render(request, "response_time/src/long_convo.html",{
				"text" : text.items(),
				"crawl": crawl, 
				"view": view,
			})

def users(request):
	return render(request, 'response_time/src/users.html', {})





