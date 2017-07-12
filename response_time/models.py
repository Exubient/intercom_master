from django.db import models

# Create your models here.

class TeamTable(models.Model):
	id = models.CharField(max_length=10, primary_key = True)
	teamName = models.CharField(max_length= 20)

	convoCount = models.IntegerField(default = 0)

	realCount = models.IntegerField(default = 0)
	averageResponseSum = models.IntegerField(default = 0)

	firstCount = models.IntegerField(default =0)
	firstResponseSum = models.IntegerField(default = 0)

	firstResponse = models.IntegerField(default=0)
	averageResponse = models.IntegerField(default=0)

	def __str__(self):
		return self.teamName

class AdminTable(models.Model):
	id = models.CharField(max_length=30, primary_key = True)
	adminName = models.CharField(max_length=30)

	convoCount = models.IntegerField(default = 0)

	realCount = models.IntegerField(default = 0)
	averageResponseSum = models.IntegerField(default = 0)

	firstCount = models.IntegerField(default =0)
	firstResponseSum = models.IntegerField(default = 0)

	firstResponse = models.IntegerField(default=0)
	averageResponse = models.IntegerField(default=0)
	medianResponse = models.IntegerField(default=0)
	teamLink = models.ForeignKey(TeamTable, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.adminName

	# startTime = models.DateTimeField()
	# endTime = models.DateTimeField()

class medianTable(models.Model):
	adminLink = models.ForeignKey(AdminTable, on_delete=models.CASCADE, null=True)
	responseTime = models.IntegerField(default=0)

class usedConvo(models.Model):
	id = models.CharField(max_length = 10, primary_key = True)
	author = models.CharField(max_length = 100, null=True)
	created_at = models.IntegerField()
	partType = models.CharField(max_length =10)
	body = models.TextField()


class Conversation(models.Model):
	id = models.TextField(primary_key = True)
	author = models.TextField()
	created_at = models.IntegerField()
	updated_at = models.IntegerField()
	parts = models.TextField()
	length = models.IntegerField()

class Conversation_part(models.Model):
	id = models.TextField(primary_key = True)
	author = models.TextField()
	created_at = models.IntegerField()
	body = models.TextField()

class LongConvo_part(models.Model):
	id = models.TextField(primary_key = True)
	author = models.TextField()
	created_at = models.IntegerField()
	body = models.TextField()

class User(models.Model):
	id = models.TextField(primary_key = True)
	created_at = models.IntegerField()
	updated_at = models.IntegerField()

class Date(models.Model):
	year = models.IntegerField()
	month = models.IntegerField()
	day = models.IntegerField()
	hour = models.IntegerField()
	minute = models.IntegerField()
