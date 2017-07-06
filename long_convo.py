from root import *

def run():
	####################################

	crawl_size = int(input("Input Size: "))
	crawl_convo(crawl_size)
	count_create()

	####################################
	long_ls=[]
	convo_count = 0
	for convo_id in recent_convo:
		convo_count += 1
		convo = intercom.conversations.find(id=convo_id)
		classConvo = Conversation(id = convo.id, created_at = convo.created_at, updated_at = convo.updated_at, author = convo.conversation_message.author, parts = convo.conversation_parts)
		print("Conversation [" + str(convo_count) +"] Len: " + str(classConvo.length))
		long_ls.append(classConvo)


	long_ls.sort(key=lambda x: x.length, reverse=True)

	for classConvo in long_ls:
		print(len(classConvo.parts))

	show_num = int(input("How many do you want to see?: "))
	
	text = str(show_num) + (" selected from recent [") + str(crawl_size) + "] conversation.\n"
	for index in range(show_num):
		text += "_____________________\n\nConversation [" + str(index) +"] Len: " + str(long_ls[index].length) +"\n"
		for x in range(len(long_ls[index].parts)):
			classParts = Conversation_part(id = long_ls[index].parts[x].id, author = long_ls[index].parts[x].author, created_at = long_ls[index].parts[x].created_at, body = long_ls[index].parts[x].body)
			text += "\nPART[" + str(x)+"]" + \
					"\nAuthor: " + str(name(classParts.author)) + \
					"\nCREATE TIME: " + str(restamp(classParts.created_at)) + \
					"\nBody: " + str(classParts.body) + "\n" 
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
			print(ValueError)
	reset()



	print("________%s seconds _______" %(time.time() - python_start))




