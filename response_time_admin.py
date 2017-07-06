from root import *

def run():
	
	####################################

	crawl_size = int(input("Input Size: "))
	crawl_name = str(input("Enter Name: "))
	admin_ls(crawl_name, crawl_size)
	count_create()


	####################################
	print(admin_convo)
	convo_count = 0
	for convo_id in admin_convo[name_dict[crawl_name]]:
		convo_count += 1
		convo = intercom.conversations.find(id=convo_id)
		classConvo = Conversation(id = convo.id, created_at = convo.created_at, updated_at = convo.updated_at, author = convo.conversation_message.author, parts = convo.conversation_parts)

		print("Conversation [" + str(convo_count) +"]")

		first_add = True
		for x in range(len(classConvo.parts)):
			classParts = Conversation_part(id = classConvo.parts[x].id, author = classConvo.parts[x].author, created_at = classConvo.parts[x].created_at, body = classConvo.parts[x].body)

			print("CONVO PART[" + str(x) + "]")
			# 2 week from today
			recent_con= start_time - 1209600 

			if (classParts.created_at > recent_con):
				if isUser(classParts.author):
					user_response = classParts.created_at
					continue
				elif isAdmin(classParts.author):
					try:
						admin_count[classParts.author.id].convo_count +=1
					except:
						pass
						
				# average_rt / average_count / median_rt
				if isAdmin(classParts.author) and (isUser(classConvo.parts[x-1].author)) and (classParts.author.id == name_dict[crawl_name]):
					admin_response = classParts.created_at
					if (admin_response - user_response <500):
						admin_count[classParts.author.id].average_time += admin_response - user_response
						admin_count[classParts.author.id].array.append(admin_response - user_response)
						admin_count[classParts.author.id].average_count += 1
						
						# first_rt / first_count 
						if first_add:
							admin_count[classParts.author.id].first_time += admin_response - user_response
							admin_count[classParts.author.id].first_count += 1
							first_add = False

				if (isAdmin(classParts.author)):
					try:
						if ((admin_count[classParts.author.id].average_count != 0) and (admin_count[classParts.author.id].first_count != 0)):
							admin_count[classParts.author.id].first_rt = admin_count[classParts.author.id].first_time / admin_count[classParts.author.id].first_count
							admin_count[classParts.author.id].average_rt = admin_count[classParts.author.id].average_time / admin_count[classParts.author.id].average_count
							admin_count[classParts.author.id].array.sort()

					except:
						admin_count[classParts.author.id] = Admin(name = "BOT", first_time = 0, first_count = 0, first_rt = 0, average_time=0, average_count = 0, average_rt = 0, array=[], convo_count = 0)


	print(send_response())

	while True:
		try:
			send = str(input("Do you want to send email?: [yes/no] "))
			if send == "yes":
				recipient = str(input("Enter Recipient: "))
				send_email(body=send_response(), recipient=recipient, crawl_size = crawl_size, file_name= os.path.basename(__file__)[:-3])
			else:
				break
		except ValueError:
			print(ValueError)
	reset()


print("________%s seconds _______" %(time.time() - python_start))




