from django.db import models

# Create your models here.
class Question(	models.Model):
	question = models.CharField(max_length = "2000")
	reponse = models.CharField(max_length = "2000")
	theme = models.CharField(max_length = "200")
	mauvaise1 = models.CharField(max_length = "2000")
	mauvaise2 = models.CharField(max_length = "2000", blank = True)
	mauvaise3 = models.CharField(max_length = "2000", blank = True)

	def __unicode__(self):
		return self.question
