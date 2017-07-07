from root import *


def run_long(crawl_size, show_num):
	####################################
	recent_convo =[]
	admin_count={}
	crawl_convo(recent_convo, crawl_size)
	count_create(admin_count)
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


	text = {}
	container=[]
	tag = ""
	for index in range(show_num):
		tag = "Conversation [" + str(index) +"] Len: " + str(long_ls[index].length)
		for x in range(len(long_ls[index].parts)):
			try:
				classPart = LongConvo_part(id = long_ls[index].parts[x].id, author = long_ls[index].parts[x].author, created_at = long_ls[index].parts[x].created_at, body = long_ls[index].parts[x].body, admin_count= admin_count)
				container.append(classPart)
			except:
				pass
		text[tag] = container
	return text





