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
    url(r'^response_time/$', views.response_time, name="response_time"),
    url(r'^start_hour/$', views.start_hour, name="start_hour"),
    url(r'^long_convo/$', views.long_convo, name="long_convo"),
    url(r'^users/$', views.users, name="users"),
]
