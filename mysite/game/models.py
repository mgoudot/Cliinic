from django.db import models
# importe le modele User pour permettre d'etendre le modele utilisateur
from django.contrib.auth.models import User

# Lorsqu'il y a une modification dans les classes et les modeles, quelle
# quelle soit, il faut executer les deux commandes suivantes dans le terminal
# dans le dossier mysite

# python manage.py schemamigration game --auto
# python migrate game


class Patient(models.Model):
	name = models.CharField(max_length=200)
	difficulty = models.PositiveIntegerField()
	active = models.BooleanField()

	def __unicode__(self):
		return self.name

# Le profil utilisateur etendu. C'est lui qui est relie et qui instancie les
# objets x-state.

class UserProfile(models.Model):
	user = models.OneToOneField(User, blank=False, null=False, default=User.objects.get(pk=1))
	rep = models.IntegerField(default=0)
	xp = models.PositiveIntegerField(default=0)

	def __unicode__(self):
		return unicode(self.user.username)


# Ceci etait une classe qui servait a dire si un patient a ete vu ou non
# par un joueur, elle est depreciee maintenant.

# class PlayerPatient(models.Model):
# 	user = models.OneToOneField(User)
# 	patient = models.ForeignKey(Patient)
# 	patientTreated = models.BooleanField()

# 	def __unicode__(self):
# 		if self.patientTreated == True:
# 			return ("%s, did see %s") % (self.user.username, self.patient)
# 		else:
# 			return ("%s, didn't see %s") % (self.user.username, self.patient)

# Le modele des maladies, lie a un patient donne.
# A une histoire liee qui sert a decrire la maladie.

class Case(models.Model):
	patient = models.ForeignKey(Patient)
	name = models.CharField(max_length=200)
	history = models.TextField()
	#difficultyRating = models.PositiveIntegerField()

	def __unicode__(self):
		return self.name

# Le modele des types d'investigation. Rien de plus a dire.

class InvestigationType(models.Model):
	name = models.CharField(max_length=200)

	def __unicode__(self):
		return self.name

# une investigation, avec son descriptif et son type.

class Investigation(models.Model):
	invtype = models.ForeignKey(InvestigationType)
	name = models.CharField(max_length=200)
	description = models.TextField()

	def __unicode__(self):
		return self.name

# les investigate, et de facon generale toutes les classes qui ont
# un verbe pour nom sont des actions du joueur, et implique le plus souvent
# un Post dans la base de donnees (l'utilisation d'un formulaire au sens large)
# Ces classes sont forcement liee e une maladie d'un patient donne.

# Le schema est "X-type" "X"(nom), "X" (verbe), puis enfin "X-state", qui va
# du plus general au plus particulier pour finir par l'instanciation.

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
	# Defining the initial status of the symptom
	BAD_STATUS = 1
	NEUTRAL_STATUS = 2
	GOOD_STATUS = 3

	SYMPTOM_STATUS = (
		(BAD_STATUS, 'Bad'),
		(NEUTRAL_STATUS, 'Neutral'),
		(GOOD_STATUS, 'Good')
	)
	initialstatus = models.IntegerField(choices=SYMPTOM_STATUS,default=1)

	name = models.CharField(max_length=200)
	patient = models.ForeignKey(Patient)
	# un Symptome est lie e un Investigate donnee, qui le decouvre (le fait passer
	# en active=True)
	# cette decouverte donne une recompense d'xp et de reputation dont le montant
	# est defini par invxp et invrep
	investigate = models.ForeignKey(Investigate, blank=True , null=True, default=None) #both null & blank needed to make foreign key field optional
	invxp = models.PositiveIntegerField(default=0)
	invrep = models.PositiveIntegerField(default=0)
	# un Symptome est soigne par un Treat donne qui le fait passe d'un etat
	# 1 a 3 (voir la classe SymptomState plus bas), avec une recompense d'xp et
	# de rep treatxp et treatrep
	treat = models.ForeignKey(Treat, blank=True, null=True, default=None)
	treatxp = models.PositiveIntegerField(default=0)
	treatrep = models.PositiveIntegerField(default=0)
	# le result est un bout de texte qui apparait et sert e donner un
	# resultat un peu detaille au joueur.
	result = models.CharField(max_length=200, default="negative")

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
	player = models.ForeignKey(User)
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

	active = models.BooleanField(default=False)
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
	investigate = models.ForeignKey(Investigate, null=True)
	active = models.BooleanField()
	player = models.ForeignKey(User)
	patient = models.ForeignKey(PatientState)
	ordered = models.BooleanField(default=False)

	def __unicode__(self):
		return unicode(self.investigate)
		
class TreatState(models.Model):
	"""docstring for TreatState"""
	treat = models.ForeignKey(Treat, null=True)
	active = models.BooleanField(default=False)
	player = models.ForeignKey(User)
	patient = models.ForeignKey(PatientState)
	ordered = models.BooleanField(default=False)

	def __unicode__(self):
		return unicode(self.treat)


		
		