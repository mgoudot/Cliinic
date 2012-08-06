from game.models import *
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


@login_required(login_url='/game/login/')
def index(request):
	patient_list = Patient.objects.all().order_by('difficulty')
	return render_to_response('game/index.html', {
	'patient_list' : patient_list,
	'hello' : request.user,
	'xp' : request.user.get_profile().xp,
	'rep' : request.user.get_profile().rep,
	},
	context_instance=RequestContext(request))


@login_required(login_url='/game/login/')
def detail(request, patient_id):
	p = get_object_or_404(Patient, pk = patient_id)
	c = p.case_set.get(pk=patient_id)
	u = request.user.get_profile()
	#Break down investigates by investigation types (lookup on the foreign key)
	#Could be more elegant by doing a double loop on investigation types and on investigates
	i_types = InvestigationType.objects.filter(investigation__investigate__patient=patient_id)
	investigations = Investigation.objects.filter(investigate__patient=patient_id)
	i = p.investigate_set.all()
	s = p.symptom_set.all()
	t = p.treat_set.all()
	return render_to_response('game/detail.html', {
	'case' : c,
	'hello' : request.user,
	'xp' : u.xp,
	'rep' : u.rep,
	'i_types' : i_types,
	'investigations' : investigations,
	'investigates' : i,
	'symptoms' : s,
	't' : t,
	},
	context_instance=RequestContext(request))


@login_required(login_url='/game/login/')
def investigate(request, patient_id):
	#allows to get and manipulate the targeted investigation.
	p = get_object_or_404(Patient, pk = patient_id)
	c = p.case_set.get(pk=patient_id)
	u = request.user.get_profile()
	i = c.investigate_set.get(id=request.POST['investigate'])
	si = i.symptom_set.all()
	for symptom in si:
		symptom.active = True
		symptom.save()
	i.ordered = True
	i.save()

	#the comparison between what's ordered and what's needed for investigations.
	if i.ordered == i.needed:
		#gets the user xp and rep counts to increase them with the reward values of each uncovered symptoms
		#pt = u.get_profile().patientsTreated
		for symptom in si:
			u.xp = u.xp + symptom.invxp
			u.rep = u.rep + symptom.invrep
			xp = u.xp
			rep = u.rep
		u.save()
		return HttpResponseRedirect('../')
		# return render_to_response('game/detail.html', {
		# 'success' : 'You succeeded ! You now have %s reputation.' % rep,
		# 'case' : c,
		# }, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('../')
		# return render_to_response('game/detail.html', {
		# 	'success' : i.ordered == i.needed,
		# 	'case' : c,
		# 	}, 
		# 	context_instance=RequestContext(request))

@login_required(login_url='/game/login/')
def treat(request, patient_id):
	#allows to get and manipulate the targeted investigation.
	p = get_object_or_404(Patient, pk = patient_id)
	c = p.case_set.get(pk=patient_id)
	u = request.user.get_profile()
	t = c.treat_set.get(id=request.POST['treat'])
	st = t.symptom_set.all()
	for symptom in st:
		symptom.status = 3
		symptom.save()
	t.ordered = True
	t.save()

	#the comparison between what's ordered and what's needed for investigations.
	if t.ordered == t.needed:
		#gets the user xp and rep counts to increase them with the reward values of each uncovered symptoms
		#pt = u.get_profile().patientsTreated
		for symptom in st:
			u.xp = u.xp + symptom.treatxp
			u.rep = u.rep + symptom.treatrep
			xp = u.xp
			rep = u.rep
		u.save()
		return HttpResponseRedirect('../')
		# return render_to_response('game/detail.html', {
		# 'success' : 'You succeeded ! You now have %s reputation.' % rep,
		# 'case' : c,
		# }, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('../')
		# return render_to_response('game/detail.html', {
		# 	'success' : i.ordered == i.needed,
		# 	'case' : c,
		# 	}, 
		# 	context_instance=RequestContext(request))


def logout_user(request):
	logout(request)
	#redirect to a success page
	return HttpResponse("Successfully logged out.")

#Strength comes from pepperonis. Don't let anyone disprove that.