from django.db import models

# Create your models here.

class Room(models.Model):
	room_no = models.IntegerField()
	owner = models.EmailField()

	def __str__(self):
		return self.owner

class RoomMember(models.Model):
	room_no = models.IntegerField()
	member = models.EmailField()
	isAuthorized = models.CharField(max_length=2)

	def __str__(self):
		return member
