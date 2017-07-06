from root import *

def run():
	####################################

	crawl_size = int(input("Input Size: "))
	crawl_user(crawl_size)

	####################################

	week={}
	for day in range(7):
		week[day] = {}
	for day in range(7):
		for time in range(23):
			week[day][time] = 0

	####################################
	new_count = 0
	update_count = 0
	user_count = 0
	for user_id in recent_user:
		user_count += 1
		user = intercom.users.find(id=user_id)
		classUser = User(user_id = user.user_id, created_at = user.created_at, updated_at = user.updated_at)
		print("User [" + str(user_count) + "]")
		sleep()
		if (start_day < classUser.created_at):
			new_count +=1
		elif (start_day < classUser.updated_at):
			update_count +=1

		print(restamp(classUser.created_at))
		classDate = Date(restamp(classUser.created_at))
		# add update
		# 따로도
		

		weekday = datetime.datetime(classDate.year, classDate.month ,classDate.day).weekday()
		week[weekday][classDate.hour] += 1

	print("WEEK:" + str(week))
	print("New user of the day:" + str(new_count))
	print("Old user of the day:" + str(update_count))


	text=""
	
	# for index in range(show_num):
	# 	text += "_____________________\n\nConversation [" + str(index) +"] Len: " + str(long_ls[index].length) +"\n"
	# 	for x in range(len(long_ls[index].parts)):
	# 		classParts = Conversation_part(id = long_ls[index].parts[x].id, author = long_ls[index].parts[x].author, created_at = long_ls[index].parts[x].created_at, body = long_ls[index].parts[x].body)
	# 		text += "\nPART[" + str(x)+"]" + \
	# 				"\nAuthor: " + str(name(classParts.author)) + \
	# 				"\nCREATE TIME: " + str(restamp(classParts.created_at)) + \
	# 				"\nBody: " + str(classParts.body) + "\n" 

	while True:
		try:
			send = str(input("Do you want to send email?: [yes/no] "))
			if send == "yes":
				recipient = str(input("Enter Recipient: "))
				send_email(body=text, recipient=recipient, crawl_size = crawl_size, file_name= os.path.basename(__file__)[:-3])
			else:
				break
		except ValueError:
			print(ValueError)
	reset()







