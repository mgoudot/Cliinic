from django.db import models
from django.contrib.auth.models import User

#python manage.py schemamigration game --auto
#python migrate game


class Patient(models.Model):
	name = models.CharField(max_length=200)
	difficulty = models.PositiveIntegerField()
	active = models.BooleanField()

	def __unicode__(self):
		return self.name


class UserProfile(models.Model):
	user = models.OneToOneField(User, blank=True, null=True, default=None)
	rep = models.IntegerField()
	xp = models.PositiveIntegerField()

	def __unicode__(self):
		return unicode(self.user.username)

# class PlayerPatient(models.Model):
# 	user = models.OneToOneField(User)
# 	patient = models.ForeignKey(Patient)
# 	patientTreated = models.BooleanField()

# 	def __unicode__(self):
# 		if self.patientTreated == True:
# 			return ("%s, did see %s") % (self.user.username, self.patient)
# 		else:
# 			return ("%s, didn't see %s") % (self.user.username, self.patient)

class Case(models.Model):
	patient = models.ForeignKey(Patient)
	name = models.CharField(max_length=200)
	history = models.TextField()
	#difficultyRating = models.PositiveIntegerField()

	def __unicode__(self):
		return self.name

class InvestigationType(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name


class Investigation(models.Model):
	invtype = models.ForeignKey(InvestigationType)
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class Investigate(models.Model):
	case = models.ForeignKey(Case)
	patient = models.ForeignKey(Patient)
	name = models.ForeignKey(Investigation)
	needed = models.BooleanField()

	def __unicode__(self):
		# unicode() method, otherwise TypeError (Investigation, not unicode)
		return unicode(self.name)

class TreatmentType(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

class Treatment(models.Model):
	treattype = models.ForeignKey(TreatmentType)
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __unicode__(self):
		return self.name

class Treat(models.Model):
	case = models.ForeignKey(Case)
	patient = models.ForeignKey(Patient)
	name = models.ForeignKey(Treatment)
	needed = models.BooleanField()

	def __unicode__(self):
		return unicode(self.name)

class Symptom(models.Model):
	name = models.CharField(max_length=200)
	patient = models.ForeignKey(Patient)
	investigate = models.ForeignKey(Investigate, blank=True , null=True, default=None) #both null & blank needed to make foreign key field optional
	invxp = models.PositiveIntegerField(default=0)
	invrep = models.PositiveIntegerField(default=0)
	treat = models.ForeignKey(Treat, blank=True, null=True, default=None)
	treatxp = models.PositiveIntegerField(default=0)
	treatrep = models.PositiveIntegerField(default=0)
	result = models.CharField(max_length=200, default="negative")
	status = models.PositiveIntegerField()

	def __unicode__(self):
		return self.name

class PatientState(models.Model):

	LOCKED_STATUS = 1
	ACTIVE_STATUS = 2
	TREATED_STATUS = 3
	CURED_STATUS = 4
	DEAD_STATUS = 5

	PATIENT_STATUS = (
		(LOCKED_STATUS, 'Locked'),
		(ACTIVE_STATUS, 'Active'),
		(TREATED_STATUS, 'Treated'),
		(CURED_STATUS, 'Cured'),
		(DEAD_STATUS, 'Dead')
	)

	patient = models.ForeignKey(Patient)
	player = models.ForeignKey(UserProfile)
	status = models.IntegerField(choices=PATIENT_STATUS, default=LOCKED_STATUS)

	def __unicode__(self):
		return "%s, %s" % (unicode(self.patient), unicode(self.player))


class SymptomState(models.Model):
	
	BAD_STATUS = 1
	NEUTRAL_STATUS = 2
	GOOD_STATUS = 3

	SYMPTOM_STATUS = (
		(BAD_STATUS, 'Bad'),
		(NEUTRAL_STATUS, 'Neutral'),
		(GOOD_STATUS, 'Good')
	)

	active = models.BooleanField()
	player = models.ForeignKey(User)
	status = models.IntegerField(choices=SYMPTOM_STATUS, null=True)
	patient = models.ForeignKey(PatientState)
	name = models.ForeignKey(Symptom)

	def __unicode__(self):
		return "%s, %s" % (unicode(self.name), unicode(self.patient))

class InvestigationState(models.Model):
	"""docstring for InvestigationState"""
	investigation = models.ForeignKey(Investigation)
	player = models.ForeignKey(User)
	available = models.BooleanField()

	def __unicode__(self):
		return unicode(self.investigation)

class TreatmentState(models.Model):
	treatment = models.ForeignKey(Treatment)
	player = models.ForeignKey(User)
	available = models.BooleanField()

	def __unicode__(self):
		return unicode(self.treatment)


class InvestigateState(models.Model):
	"""docstring for InvestigateState"""
	active = models.BooleanField()
	player = models.ForeignKey(User)
	patient = models.ForeignKey(PatientState)
	name = models.ForeignKey(InvestigationState)
	ordered = models.BooleanField()

	def __unicode__(self):
		return unicode(self.name)
		
class TreatState(models.Model):
	"""docstring for TreatState"""
	active = models.BooleanField()
	player = models.ForeignKey(User)
	patient = models.ForeignKey(PatientState)
	name = models.ForeignKey(TreatmentState)
	ordered = models.BooleanField()

	def __unicode__(self):
		return unicode(self.name)


		
		