from django.shortcuts import render
from django.shortcuts import get_object_or_404

from response_time.models import AdminTable

from root import *
from time_response import run_response
from long_convo import run_long
from start_time import run_start
from new_user import run_start



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
				# "crawl_list" : crawl_dict.items(),
			})


def start_hour(request):
	if request.method =="GET":
		return render(request, 'response_time/src/start_hour.html', {})
	elif request.method =="POST":
		crawl_name = request.POST.get("crawl_name")
		crawl_text = run_start(crawl_name)
		return render(request, "response_time/src/start_hour.html",{
				"crawl_text" : crawl_text,
			})

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
	if request.method =="GET":
		return render(request, 'response_time/src/users.html', {})

	if request.method == "POST":
		crawl_size = int(request.POST.get("crawl_size"))
		text = run_start(crawl_size)
		new = {}
		update = {}
		for a in range(7):
			new[a] = 1
			update[a] =3
		return render(request, "response_time/src/users.html",{
				"text" : text,
				"new" : new,
				"update" : update,
			})





