from intercom.client import Client
import time
import datetime
import inspect
from bs4 import BeautifulSoup
import os
import statistics
from response_time.models import AdminTable, usedConvo, medianTable


####################################################
python_start=time.time()
localtime = 32400
day = 86400
NoneType = type(None)	
intercom = Client(personal_access_token='dG9rOjQ2NjNjNzhhXzBkYjFfNDBjMF9iYWYyXzI3YjVhOTVmMzUyMToxOjA=')
convo_tmp = intercom.conversations.find(id="10512241549")

####################################################

def stamp(date):
	if isinstance(date, str):
		return time.mktime(datetime.datetime.strptime(date, "%Y/%m/%d %H:%M:%S").timetuple())
	elif isinstance(date, datetime.datetime):
		return time.mktime(date.timetuple())

def restamp(date):
	return datetime.datetime.fromtimestamp(int(date)).strftime('%Y/%m/%d %H:%M:%S')

def localize(date):
	return stamp(date) + localtime

def sleep():
	time.sleep(0.5)

####################################################

start_time = stamp(restamp(time.time())[:-8] + "6:0:0")
start_day = stamp(restamp(time.time())[:-8] + "0:0:0")


####################################################

# admin_office = {}
def admin_officehour(admin_office):
	for admin in intercom.admins.all():
		admin_office[admin.id] = AdminHour(name = admin.name, start = 0, end = 0, array=[])

####################################################

# recent_convo =[]
def crawl_convo(array, crawl_size):
	for convo in intercom.conversations.find_all():
		if len(array) < crawl_size:
			array.append(convo.id)
		else:
			break

# recent_user =[]
def crawl_user(crawl_size, recent_user):
	for user in intercom.users.find_all():
		if len(recent_user) < crawl_size:
			recent_user.append(user.id)
		else:
			break

####################################################

# name_dict={}
# admin_convo = {}
def admin_ls(nombre, crawl_size, admin_convo):
	for admin in intercom.admins.all():
		if admin.name == nombre:
			ls=[]
			for convo in intercom.conversations.find_all(type="admin", admin_id=admin.id):
				if (len(ls)< crawl_size):
					ls.append(convo.id)
					sleep()
				else:
					break
				admin_convo[admin.id] = ls
				sleep()

####################################################

def isAdmin(input):
	adminType = type(convo_tmp.assignee)
	if type(input) == adminType:
		return True
	else:
		return False

def isUser(input):
	userType = type(convo_tmp.user)
	if type(input) == userType:
		return True
	else:
		return False

def isBot(input):
	if not isAdmin(input) and not isUser(input):
		return True
	else:
		return False

####################################################

class Conversation():
	def __init__(self, id, created_at, updated_at, author, parts):
		self.id = id
		self.author = author
		self.created_at = localize(created_at)
		self.updated_at = localize(updated_at)
		self.parts = parts
		self.length = len(parts)

class Conversation_part():
	def __init__(self, id, author, created_at, body, partType):
		self.id = id
		self.author = author
		self.created_at = localize(created_at)
		self.partType = partType
		if type(body) != NoneType:
			self.body = BeautifulSoup(body, "html5lib").get_text()
		else:
			self.body = "NONE"

class LongConvo_part():
	def __init__(self, id, author, created_at, body, admin_count):
		self.id = id
		self.author = name(author, admin_count)
		self.created_at = restamp(localize(created_at))
		if type(body) != NoneType:
			self.body = BeautifulSoup(body, "html5lib").get_text()
		else:
			self.body = "NONE"
class Admin():
	def __init__(self, name, first_time, first_count, first_rt, array, average_time, average_count, average_rt, convo_count, median_rt):
		self.name = name
		self.first_time = first_time
		self.first_count = first_count
		self.first_rt = first_rt
		self.array = array
		self.average_rt = average_rt
		self.average_count = average_count
		self.average_time = average_time
		self.convo_count = convo_count
		self.median_rt = median_rt

class AdminHour():
	def __init__(self, name, start, end, array):
		self.name = name
		self.start = start
		self.end = end
		self.array = array

class User():
	def __init__(self, user_id, created_at, updated_at):
		self.name = user_id
		self.created_at = localize(created_at)
		self.updated_at = localize(updated_at)

class Date():
	def __init__(self, data):
		self.year = int(data[0:4])
		self.month = int(data[5:7])
		self.day = int(data[8:10])
		self.hour = int(data[11:13])
		self.minute = int(data[14:16])

####################################################

# def name(data, admin_count):
# 	try:
# 		if isUser(data):
# 			return "SOME USER"
# 		elif isAdmin(data):
# 			return admin_count[data.id].name
# 	except:
# 			return "NAME ERROR"

def send_response(dict):
	text=""	
	for key, item in dict.items():
		if (item.average_rt != 0):
			if ((len(item.array)/2)%2 == 1):
				text += "\nADMIN ID: " + str(key) + \
					"\nADMIN NAME: " + str(item.name) + \
					"\nALL CONVO COUNT: " + str(item.convo_count) + \
					"\nREAL CONVO COUNT: " + str(item.average_count) +\
					"\nFIRST RESPONSE TIME: " + str(item.first_rt) + \
					"\nAVERAGE RESPONSE TIME: " + str(item.average_rt) + \
					"\nMEDIAN RESPONSE TIME: " + str(item.array[int((len(item.array)-1)/2)]) + \
					"\n____________________\n"
			else:
				text += "\nADMIN ID: " + str(key) + \
					"\nADMIN NAME: " + str(item.name) + \
					"\nALL CONVO COUNT: " + str(item.convo_count) + \
					"\nREAL CONVO COUNT: " + str(item.average_count) +\
					"\nFIRST RESPONSE TIME: " + str(item.first_rt) + \
					"\nAVERAGE RESPONSE TIME: " + str(item.average_rt) + \
					"\nMEDIAN RESPONSE TIME: " + str(item.array[int(len(item.array)/2)]) + \
					"\n____________________\n"
	return text

def export():
	for admin in AdminTable.objects.all():
		# average response time
		if admin.realCount != 0:
			admin.averageResponse = admin.averageResponseSum / admin.realCount
		# first response time 
		if admin.firstCount != 0:
			admin.firstResponse = admin.firstResponseSum / admin.firstCount
		# median response time
		ls = [convo.responseTime for convo in medianTable.objects.filter(adminLink = admin.id)]
		if len(ls)!=0:
			admin.medianResponse = statistics.median(ls)
		admin.save()






