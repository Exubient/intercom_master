from root import *
from response_time.models import AdminTable, usedConvo, medianTable

def name(data):
	if isUser(data):
		return "User"
	elif isBot(data):
		return "BOT"
	elif AdminTable.objects.filter(id = data.id).exists():
		name = AdminTable.objects.get(id = data.id)
		return name.adminName
def getComment(data):
	return 

def run_response(crawl_size):

	####################################
	recent_convo =[]
	crawl_convo(recent_convo, crawl_size)

	####################################

	for convo_id in recent_convo:
		convo = intercom.conversations.find(id=convo_id)
		classConvo = Conversation(id = convo.id, created_at = convo.created_at, updated_at = convo.updated_at, author = convo.conversation_message.author, parts = convo.conversation_parts)

		first_add = True
		for x in range(len(classConvo.parts)):
			classParts = Conversation_part(id = classConvo.parts[x].id, author = classConvo.parts[x].author, created_at = classConvo.parts[x].created_at, body = classConvo.parts[x].body, partType = classConvo.parts[x].part_type)
			if usedConvo.objects.filter(id = classParts.id).exists():
				print("----------- 존재하는 대화 -----------")
				continue
			else:
				#Save to postgres DB
				convoSave = usedConvo(id = classParts.id, author = name(classParts.author), created_at = classParts.created_at, body = classParts.body, partType = classParts.partType)
				convoSave.save()

				if isUser(classParts.author):
					user_response = classParts.created_at
					continue

				if classParts.partType =="note":
					continue

				if AdminTable.objects.filter(id = classParts.author.id).exists():
					tmpAdmin = AdminTable.objects.get(id = classParts.author.id)
					if isAdmin(classParts.author):
						tmpAdmin.convoCount += 1

						if (isUser(classConvo.parts[x-1].author)):
							admin_response = classParts.created_at
							tmpAdmin.averageResponseSum += admin_response - user_response
							tmpAdmin.realCount += 1

							medianSave = medianTable(adminLink = tmpAdmin, responseTime = admin_response - user_response)
							medianSave.save()

							# admin_count[classParts.author.id].array.append(admin_response - user_response)
					
							if first_add:
								tmpAdmin.firstResponseSum += admin_response - user_response
								tmpAdmin.firstCount += 1
								first_add = False

					tmpAdmin.save()
				else:
					print("no admin")
							# admin_count[classParts.author.id].average_rt = admin_count[classParts.author.id].average_time / admin_count[classParts.author.id].average_count
							# admin_count[classParts.author.id].array.sort()


						# if ((len(admin_count[classParts.author.id].array))%2 == 1):
						# 	admin_count[classParts.author.id].median_rt = admin_count[classParts.author.id].array[int((len(admin_count[classParts.author.id].array)+1)/2)]
						# else:
						# 	admin_count[classParts.author.id].median_rt = admin_count[classParts.author.id].array[int(len(admin_count[classParts.author.id].array)/2)]
				
		return True


	# while True:
	# 	try:
	# 		send = str(input("Do you want to send email?: [yes/no] "))
	# 		if send == "yes":
	# 			recipient = str(input("Enter Recipient: "))
	# 			send_email(body=send_response(), recipient=recipient, crawl_size = crawl_size, file_name= os.path.basename(__file__)[:-3])
	# 		else:
	# 			break
	# 	except ValueError:
	# 		print(ValueError)




	print("________%s seconds _______" %(time.time() - python_start))



