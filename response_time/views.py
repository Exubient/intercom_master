from django.shortcuts import render
from django.shortcuts import get_object_or_404
from root import *
from rt import run_response

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


def response_time_admin(request):
	return render(request, 'response_time/src/response_time_admin.html', {})

def start_hour(request):
	return render(request, 'response_time/src/start_hour.html', {})

def long_convo(request):
	return render(request, 'response_time/src/long_convo.html', {})

def users(request):
	return render(request, 'response_time/src/users.html', {})





