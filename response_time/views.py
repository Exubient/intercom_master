from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import Q

from response_time.models import AdminTable, medianTable, TeamTable

from algo.root import *
from algo.time_response import run_response
from algo.long_convo import run_long
from algo.start_time import run_start
from algo.new_user import run_start

############################## ############################## ############################## ############################## 
def root(request):
	if request.method =="GET":
		return render(request, 'response_time/src/etc/root.html', {})
	elif request.method == "POST":
		reset()
		return render(request, 'response_time/src/etc/root.html', {})

############################## ############################## ############################## ############################## 

def response_team(request):	
	teamObject={}
	for team in TeamTable.objects.filter(~Q(realCount=0)):
		teamObject[team.teamName] = [team.convoCount, team.realCount, team.firstCount, team.firstResponse, team.averageResponse]

	return render(request, "response_time/src/response/response_team.html",{
			"adminObject" : teamObject.items(),
		})


############################## ############################## ############################## ############################## 

def response_CleanerCare(request):	
	adminObject={}
	for admin in AdminTable.objects.filter(~Q(realCount=0)):
		if str(admin.teamLink) == "Cleaner Care":
			adminObject[admin.adminName] = [admin.convoCount, admin.realCount, admin.firstCount, admin.firstResponse, admin.averageResponse, admin.medianResponse]

	return render(request, "response_time/src/response/response_cleanercare.html",{
			"adminObject" : adminObject.items(),
		})

def response_CustomerSales(request):	
	adminObject={}
	for admin in AdminTable.objects.filter(~Q(realCount=0)):
		if str(admin.teamLink) == "Customer Sales":
			adminObject[admin.adminName] = [admin.convoCount, admin.realCount, admin.firstCount, admin.firstResponse, admin.averageResponse, admin.medianResponse]

	return render(request, "response_time/src/response/response_customersales.html",{
			"adminObject" : adminObject.items(),
		})

def response_CustomerSupport(request):	
	adminObject={}
	for admin in AdminTable.objects.filter(~Q(realCount=0)):
		if str(admin.teamLink) == "Customer Support":
			adminObject[admin.adminName] = [admin.convoCount, admin.realCount, admin.firstCount, admin.firstResponse, admin.averageResponse, admin.medianResponse]

	return render(request, "response_time/src/response/response_customersupport.html",{
			"adminObject" : adminObject.items(),
		})

def response_Telecommuting(request):	
	adminObject={}
	for admin in AdminTable.objects.filter(~Q(realCount=0)):
		if str(admin.teamLink) == "Telecommuting":
			adminObject[admin.adminName] = [admin.convoCount, admin.realCount, admin.firstCount, admin.firstResponse, admin.averageResponse, admin.medianResponse]

	return render(request, "response_time/src/response/response_telecommuting.html",{
			"adminObject" : adminObject.items(),
		})


############################## ############################## ############################## ############################## 
def response_teammate(request):
	adminObject={}
	for admin in AdminTable.objects.filter(~Q(firstCount=0)).filter(~Q(realCount=0)):
		adminObject[admin.adminName] = [admin.convoCount, admin.realCount, admin.firstCount, admin.firstResponse, admin.averageResponse, admin.medianResponse]

	return render(request, "response_time/src/response/response_teammate.html",{
			"adminObject" : adminObject.items(),
		})

def response_weekly(request):
	if request.method =="GET":
		adminObject={}
		for admin in AdminTable.objects.filter(~Q(firstCount=0)).filter(~Q(realCount=0)):
			adminObject[admin.adminName] = [admin.convoCount, admin.realCount, admin.firstCount, admin.firstResponse, admin.averageResponse, admin.medianResponse]

		return render(request, "response_time/src/response/response_weekly.html",{
				"adminObject" : adminObject.items(),
			})

	elif request.method == "POST":
		run_response(1)
		export()
		adminObject={}
		for admin in AdminTable.objects.filter(~Q(firstCount=0)).filter(~Q(realCount=0)):
			adminObject[admin.adminName] = [admin.convoCount, admin.realCount, admin.firstCount, admin.firstResponse, admin.averageResponse, admin.medianResponse]

		return render(request, "response_time/src/response/response_weekly.html",{
				"adminObject" : adminObject.items(),
			})

############################## ############################## ############################## ##############################

def start_team(request):
	if request.method =="GET":
		return render(request, 'response_time/src/start/start_team.html', {})
	elif request.method =="POST":
		crawl_name = request.POST.get("crawl_name")
		crawl_text = run_start(crawl_name)
		return render(request, "response_time/src/start/start_team.html",{
				"crawl_text" : crawl_text,
			})

def start_teammate(request):
	if request.method =="GET":
		return render(request, 'response_time/src/start/start_teammate.html', {})
	elif request.method =="POST":
		crawl_name = request.POST.get("crawl_name")
		crawl_text = run_start(crawl_name)
		return render(request, "response_time/src/start/start_teammate.html",{
				"crawl_text" : crawl_text,
			})

############################## ############################## ############################## ############################## 

def users_weekly(request):
	if request.method =="GET":
		return render(request, 'response_time/src/users/users_weekly.html', {})

	if request.method == "POST":
		crawl_size = int(request.POST.get("crawl_size"))
		text = run_start(crawl_size)
		new = {}
		update = {}
		for a in range(7):
			new[a] = 1
			update[a] =3
		return render(request, "response_time/src/users/users_weekly.html",{
				"text" : text,
				"new" : new,
				"update" : update,
			})

def users_hourly(request):
	if request.method =="GET":
		return render(request, 'response_time/src/users/users_hourly.html', {})

	if request.method == "POST":
		crawl_size = int(request.POST.get("crawl_size"))
		text = run_start(crawl_size)
		new = {}
		update = {}
		for a in range(7):
			new[a] = 1
			update[a] =3
		return render(request, "response_time/src/users/users_hourly.html",{
				"text" : text,
				"new" : new,
				"update" : update,
			})

############################## ############################## ############################## ############################## 

def long_convo(request):
	if request.method =="GET":
		return render(request, 'response_time/src/convo/long_convo.html', {})

	if request.method == "POST":
		crawl = int(request.POST.get("crawl"))
		view = int(request.POST.get("view"))	
		text = run_long(crawl, view)

		return render(request, "response_time/src/convo/long_convo.html",{
				"text" : text.items(),
				"crawl": crawl, 
				"view": view,
			})



