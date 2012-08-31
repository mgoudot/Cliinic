from polls.models import *
from game.models import *
from versus.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from website.game.models import UserProfile

admin.site.unregister(User) 

class UserProfileInline(admin.StackedInline):
	model = UserProfile


class UserProfileAdmin(admin.ModelAdmin):
	inlines = [UserProfileInline]

####### All the patient admin
class SymptomInline(admin.TabularInline):
	model = Symptom
	extra = 0

# class SymptomAdmin(admin.ModelAdmin):
# 	list_display= ('name',)
# 	inlines = [SymptomInline,]

class CaseInline(admin.TabularInline):
	model = Case
	extra = 0


class InvestigateInline(admin.TabularInline):
	model = Investigate
	extra = 1

class TreatInline(admin.TabularInline):
	model = Treat
	extra = 0

# class InvestigationToDoInline(admin.TabularInline):
# 	model = InvestigationToDo


class PatientAdmin(admin.ModelAdmin):
	list_display = ('name', 'difficulty', 'active')
	fieldsets = [
	('Hello', {'fields': ['name', 'difficulty', 'active']}),	
	]
	inlines = [CaseInline, InvestigateInline, SymptomInline, TreatInline ]

####### InvestigationType admin, serves as investigation manager 

class InvestigationInline(admin.TabularInline):
	model = Investigation

class InvestigationTypeInline(admin.StackedInline):
	model = InvestigationType
	extra = 0

class InvestigationAdmin(admin.ModelAdmin):
	list_display = ('name','invtype')
	fieldsets = [
	('Hello', {'fields': ['name', 'invtype', 'description']}),
	]

class InvestigationTypeAdmin(admin.ModelAdmin):
		fieldsets = [
	('Hello', {'fields': ['name']}),
	]

####### Treatment admin, serves as treatment manager 

class TreatmentInline(admin.TabularInline):
	model = Treatment

class TreatmentTypeInline(admin.StackedInline):
	model = TreatmentType
	extra = 0

class TreatmentAdmin(admin.ModelAdmin):
	list_display = ('name','treattype')
	fieldsets = [
	('Hello', {'fields': ['name', 'treattype', 'description']}),
	]

class TreatmentTypeAdmin(admin.ModelAdmin):
		fieldsets = [
	('Hello', {'fields': ['name']}),
	]

####### The X-state admin, serves as player-level manager

class SymptomStateInline(admin.TabularInline):
	model = SymptomState
	extra = 0

class InvestigateStateInline(admin.TabularInline):
	model = InvestigateState
	extra = 0

class TreatStateInline(admin.TabularInline):
	model = TreatState
	extra = 0

class PatientStateAdmin(admin.ModelAdmin):
	list_display = ('patient', 'player', 'status')
	fieldsets = [
	('Hello', {'fields': ['patient', 'player', 'status']}),	
	]
	inlines = [SymptomStateInline, InvestigateStateInline, TreatStateInline]


admin.site.register(User, UserProfileAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(InvestigationType, InvestigationTypeAdmin)
admin.site.register(Investigation, InvestigationAdmin)
admin.site.register(TreatmentType, TreatmentTypeAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(PatientState, PatientStateAdmin)

# class PollAdmin(admin.ModelAdmin):
# 	#fields = ['pub_date', 'question']
# 	fieldsets = [
# 		('Poulpe', {'fields': ['question']}),
# 		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
# 	]
# 	inlines = [ChoiceInline]
# 	list_display = ('question', 'pub_date', 'was_published_today')
# 	list_filter = ['pub_date']
# 	search_fields = ['question']
# 	date_hierarchy = 'pub_date'

# class VersusAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 	('question', {'fields': ['question']}),
# 	('theme', {'fields':['theme']}),
# 	('reponse', {'fields':['reponse']}),
# 	('mauvaise1', {'fields' : ['mauvaise1']}),
# 	('mauvaise2', {'fields' : ['mauvaise2']}),
# 	('mauvaise3', {'fields' : ['mauvaise3']})
# 	]
# 	list_display = ('question', 'theme')
# 	list_filter = ['theme']

# class ChoiceInline(admin.TabularInline):
# 	model = Choice
# 	extra = 3