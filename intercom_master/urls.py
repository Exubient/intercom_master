"""intercom_master URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from response_time import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.root, name="root"),
    
    url(r'^response_time/team$', views.response_team, name="rt_team"),

    url(r'^response_time/team/CleanerCare$', views.response_CleanerCare, name="rt_CleanerCare"),
    url(r'^response_time/team/CustomerSales$', views.response_CustomerSales, name="rt_CustomerSales"),
    url(r'^response_time/team/CustomerSupport$', views.response_CustomerSupport, name="rt_CustomerSupport"),
    url(r'^response_time/team/Telecommuting$', views.response_Telecommuting, name="rt_Telecommuting"),

    url(r'^response_time/teammate$', views.response_teammate, name="rt_teammate"),
    url(r'^response_time/weekly$', views.response_weekly, name="rt_weekly"),

    url(r'^start_hour/team$', views.start_team, name="start_team"),
    url(r'^start_hour/teammate$', views.start_teammate, name="start_teammate"),

    url(r'^users/weekly$', views.users_weekly, name="users_weekly"),
    url(r'^users/hourly$', views.users_hourly, name="users_hourly"),

    url(r'^long_convo/$', views.long_convo, name="long_convo"),
]
