from algo.root import *
from response_time.models import AdminTable, usedConvo, medianTable
	
def name(data):
	if isUser(data):
		return "User"
	elif isBot(data):
		return "BOT"
	elif AdminTable.objects.filter(id = data.id).exists():
		name = AdminTable.objects.get(id = data.id)
		return name.adminName

def saveConvo(classParts):
	convoSave = usedConvo(id = classParts.id, author = name(classParts.author), created_at = classParts.created_at, body = classParts.body, partType = classParts.partType)
	convoSave.save()

def saveMedian(tmpAdmin, admin_response, user_response):
	medianSave = medianTable(adminLink = tmpAdmin, responseTime = admin_response - user_response)
	medianSave.save()

def ConvoCreate(convo_id):
	convo = intercom.conversations.find(id=convo_id)
	return Conversation(id = convo.id, created_at = convo.created_at, updated_at = convo.updated_at, author = convo.conversation_message.author, parts = convo.conversation_parts)

def PartCreate(classConvo, x):
	return Conversation_part(id = classConvo.parts[x].id, author = classConvo.parts[x].author, created_at = classConvo.parts[x].created_at, body = classConvo.parts[x].body, partType = classConvo.parts[x].part_type)

def partExist(classParts):
	return usedConvo.objects.filter(id = classParts.id).exists()

def run_response(crawl_size):

	####################################
	recent_convo =[]
	crawl_convo(recent_convo, crawl_size)

	####################################

	for convo_id in recent_convo:
		classConvo = ConvoCreate(convo_id)

		first_add = True
		user_start = False
		for index in range(len(classConvo.parts)):
			classParts = PartCreate(classConvo, index)

			if partExist(classParts):
				continue
			else:
				saveConvo(classParts)

				if isUser(classParts.author):
					user_response = classParts.created_at
					user_start = True
					continue
				if user_start:
					if classParts.partType =="note":
						continue

					if AdminTable.objects.filter(id = classParts.author.id).exists():
						tmpAdmin = AdminTable.objects.get(id = classParts.author.id)
						
						if isAdmin(classParts.author):
							tmpAdmin.convoCount += 1
							if (isUser(classConvo.parts[index-1].author)):
								admin_response = classParts.created_at
								delta = admin_response - user_response
								if delta < 500:
									tmpAdmin.averageResponseSum += delta
									tmpAdmin.realCount += 1
									saveMedian(tmpAdmin, admin_response, user_response)
							
									if first_add:
										tmpAdmin.firstResponseSum += delta
										tmpAdmin.firstCount += 1
										first_add = False
						tmpAdmin.save()
				else:
					print("__Deleted Admin__")






