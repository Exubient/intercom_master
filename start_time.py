from root import *

def run():
	
	####################################

	crawl_name = str(input("Enter Name: "))
	crawl_size = 50
	admin_ls(crawl_name, crawl_size)
	admin_officehour()

	####################################
	print(admin_convo)
	convo_count = 0
	for convo_id in admin_convo[name_dict[crawl_name]]:

		convo_count += 1
		convo = intercom.conversations.find(id=convo_id)
		classConvo = Conversation(id = convo.id, created_at = convo.created_at, updated_at = convo.updated_at, author = convo.conversation_message.author, parts = convo.conversation_parts)

		print("Conversation [" + str(convo_count) +"]")

		for x in range(len(classConvo.parts)):
			classParts = Conversation_part(id = classConvo.parts[x].id, author = classConvo.parts[x].author, created_at = classConvo.parts[x].created_at, body = classConvo.parts[x].body)
			if (classParts.author.id == name_dict[crawl_name]):
				if ((classParts.created_at > start_time - day) and (classParts.created_at < start_time)):
					admin_office[classParts.author.id].array.append(classParts.created_at)
	if len(admin_office[name_dict[crawl_name]].array) > 1:
		admin_office[name_dict[crawl_name]].start = min(admin_office[name_dict[crawl_name]].array)
		admin_office[name_dict[crawl_name]].end = max(admin_office[name_dict[crawl_name]].array)
	else:
		print("No convo")
		return

	text=""
	text += "\n[" + crawl_name +"]\n출근시간 :"+ restamp(admin_office[name_dict[crawl_name]].start) + "\n퇴근시간: " + \
			restamp(admin_office[name_dict[crawl_name]].end) 


	print(text)
	while True:
		try:
			send = str(input("Do you want to send email?: [yes/no] "))
			if send == "yes":
				recipient = str(input("Enter Recipient: "))
				send_email(body=text, recipient=recipient, crawl_size = crawl_size, file_name= os.path.basename(__file__)[:-3])
			else:
				break
		except ValueError:
			print('2')
	reset()


	print("________%s seconds _______" %(time.time() - python_start))




