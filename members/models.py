from django.db import models

class Member(models.Model):
	# essential 
	uid		= models.CharField(max_length=15)
	password	= models.CharField(max_length=20)
	name		= models.CharField(max_length=15)
	
	# option
	age		= models.IntegerField(default=0)
	gender		= models.CharField(max_length=8)

	# log
	total_points	= models.IntegerField(default=0)
	level		= models.IntegerField(default=1)
	levelName	= models.CharField(max_length=10)
	
	# savings
	points		= models.IntegerField(default=0)


	def __str__(self):
		return self.uid
