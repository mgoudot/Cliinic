from versus.models import *
from django.contrib import admin

class VersusAdmin(admin.ModelAdmin):
	fieldsets = [
	('question', {'fields': ['question']}),
	('theme', {'fields':['theme']}),
	('reponse', {'fields':['reponse']}),
	('mauvaise1', {'fields' : ['mauvaise1']}),
	('mauvaise2', {'fields' : ['mauvaise2']}),
	('mauvaise3', {'fields' : ['mauvaise3']})
	]
	list_display = ('question', 'theme')
	list_filter = ['theme']
	
admin.site.register(Question, VersusAdmin)