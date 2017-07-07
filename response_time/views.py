from django.shortcuts import render
from django.shortcuts import get_object_or_404
from root import *
from time_response import run_response
from long_convo import run_long
from start_time import run_start
from new_user import run_start

# fusion charts api
from fusioncharts import FusionCharts


# Create your views here.

column2d = FusionCharts("column2d", "ex1" , "600", "400", "chart-1", "json", 
        """{  
               "chart":
               {  
                  "caption":"Harry's SuperMart",
                  "subCaption":"Top 5 stores in last month by revenue",
                  "numberPrefix":"$",
                  "theme":"ocean"
               },
               "data":
               [  
                  {  
                     "label":"Bakersfield Central",
                     "value":"880000"
                  },
                  {  
                     "label":"Garden Groove harbour",
                     "value":"730000"
                  },
                  {  
                     "label":"Los Angeles Topanga",
                     "value":"590000"
                  },
                  {  
                     "label":"Compton-Rancho Dom",
                     "value":"520000"
                  },
                  {  
                     "label":"Daly City Serramonte",
                     "value":"330000"
                  }
               ]
        }""")





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

		return render(request, "response_time/src/users.html",{
				"text" : text,
				"column2d" : column2d.render(),
			})





