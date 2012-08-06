from django.db import models
import datetime

class Poll(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	
	def __unicode__(self):
		return self.question
	
	def was_published_today(self):
		return self.pub_date.date() == datetime.date.today()
	was_published_today.short_description = 'Published today?'
	
class Choice(models.Model):
	poll = models.ForeignKey(Poll)
	choice = models.CharField(max_length=200)
	votes = models.IntegerField()
	
	def __unicode__(self):	
		return self.choice

"""class Patient(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Case(models.Model):
	patient = models.ForeignKey(Patient)
	name = models.CharField(max_length=200)
	history = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Investigate(models.Model):
	case = models.ForeignKey(Case)
	patient = models.ForeignKey(Patient)
	name = models.CharField(max_length=200)
	todo = models.BooleanField()

	def __unicode__(self):
		return self.name"""