from django.db import models

# Create your models here.

class Admin(models.Model):
	id = models.TextField(primary_key = True)
	name = models.TextField()

	first_time = models.FloatField()
	first_count = models.FloatField()
	first_rt = models.FloatField()

	average_time = models.FloatField()
	average_count = models.FloatField()
	averate_rt = models.FloatField()
	convo_count  = models.FloatField()

	array = models.TextField()

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

class AdminHour(models.Model):
	name = models.TextField()
	start = models.IntegerField()
	end = models.IntegerField()
	array = models.TextField()

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
