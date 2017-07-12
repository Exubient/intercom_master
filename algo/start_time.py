from algo.root import *

def run_start(crawl_name):
	
	####################################
	crawl_size = 20
	admin_convo={}
	admin_ls(crawl_name, crawl_size, admin_convo)
	admin_office={}
	admin_officehour(admin_office)

	####################################

	convo_count = 0

	for key, item in admin_convo.items():
		for convo_id in item:
			convo_count += 1
			convo = intercom.conversations.find(id=convo_id)
			classConvo = Conversation(id = convo.id, created_at = convo.created_at, updated_at = convo.updated_at, author = convo.conversation_message.author, parts = convo.conversation_parts)

			print("Conversation [" + str(convo_count) +"]")

			for x in range(len(classConvo.parts)):
				classParts = Conversation_part(id = classConvo.parts[x].id, author = classConvo.parts[x].author, created_at = classConvo.parts[x].created_at, body = classConvo.parts[x].body)
				if (classParts.author.id == key):
					if ((classParts.created_at > start_time - day) and (classParts.created_at < start_time)):
						print(restamp(classParts.created_at))
						admin_office[classParts.author.id].array.append(classParts.created_at)
		if len(admin_office[key].array) > 1:
			admin_office[key].start = min(admin_office[key].array)
			admin_office[key].end = max(admin_office[key].array)
		else:
			print("No convo")
			return

		crawl_dict = {}
		text += "\n[" + crawl_name +"]\n출근시간 :"+ restamp(admin_office[key].start) + "\n퇴근시간: " + \
				restamp(admin_office[key].end) 
		return text







