from django.db import models

# Create your models here.

class AdminTable(models.Model):
	id = models.CharField(max_length=30, primary_key = True)
	adminName = models.CharField(max_length=30)

	convoCount = models.FloatField(default = 0)

	realCount = models.FloatField(default = 0)
	firstCount = models.FloatField(default =0)

	firstResponseSum = models.FloatField(default = 0)
	averageResponseSum = models.FloatField(default = 0)

	medianResponseSum = models.FloatField(default = 0)

	firstResponse = models.FloatField(default=0)
	averageResponse = models.FloatField(default=0)
	medianResponse = models.FloatField(default=0)

	# startTime = models.DateTimeField()
	# endTime = models.DateTimeField()


class usedConvo(models.Model):
	id = models.CharField(max_length = 10, primary_key = True)
	author = models.CharField(max_length = 100, null=True)
	created_at = models.IntegerField()
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
