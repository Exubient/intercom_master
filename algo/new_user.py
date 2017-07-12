from algo.root import *

def run_start(crawl_size):
	####################################
	recent_user =[]
	crawl_user(crawl_size, recent_user)

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

	return (str(week))






