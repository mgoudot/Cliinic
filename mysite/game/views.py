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
	# I just read that using get_or_create shouldn't be done in Django views.
	# So we should find another way to instantiate everything
	pstate, created= p.patientstate_set.get_or_create(patient=p, player=request.user)
	c = p.case_set.get(pk=patient_id)
	u = request.user.get_profile()
	#Break down investigates by investigation types (lookup on the foreign key)
	#Could be more elegant by doing a double loop on investigation types and on investigates
	i_types = InvestigationType.objects.filter(investigation__investigate__patient=patient_id).distinct()
	investigations = Investigation.objects.filter(investigate__patient=patient_id)
	i = p.investigate_set.all()
	s = p.symptom_set.all()
	sstates = []
	for symptom in s:
		sstate, created = symptom.symptomstate_set.get_or_create(player=request.user, patient=pstate, name=symptom, defaults={'status' : symptom.initialstatus})
		if symptom.investigate == None:
			sstates.append(sstate)
		elif sstate.active ==True:
			sstates.append(sstate)
	t = p.treat_set.all()
	return render_to_response('game/detail.html', {
	'case' : c,
	'hello' : request.user,
	'xp' : u.xp,
	'rep' : u.rep,
	'i_types' : i_types,
	'investigations' : investigations,
	'investigates' : i,
	'symptoms' : sstates,
	't' : t,
	},
	context_instance=RequestContext(request))


@login_required(login_url='/game/login/')
def investigate(request, patient_id):
	#allows to get and manipulate the targeted investigation.
	p = get_object_or_404(Patient, pk = patient_id)
	# the get_or_create methods returns the object and a boolean that indicates if the creation happened.
	pstate, created= p.patientstate_set.get_or_create(patient=p, player=request.user)
	c = p.case_set.get(pk=patient_id)
	u = request.user.get_profile()
	i = c.investigate_set.get(id=request.POST['investigate'])
	si = i.symptom_set.all()
	for symptom in si:
		ss, created = symptom.symptomstate_set.get_or_create(player=request.user, patient=pstate, name=symptom, defaults={'status' : symptom.initialstatus})
		ss.active = True
		ss.save()
	istate, created = i.investigatestate_set.get_or_create(player=request.user, patient=pstate, investigate=i)
	istate.ordered = True
	istate.save()

	#the comparison between what's ordered and what's needed for investigations.
	if istate.ordered == i.needed:
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
	pstate, created = p.patientstate_set.get_or_create(patient=p, player=request.user)
	c = p.case_set.get(pk=patient_id)
	u = request.user.get_profile()
	t = c.treat_set.get(id=request.POST['treat'])
	tstate, created = t.treatstate_set.get_or_create(player=request.user, treat=t, patient=pstate)
	st = t.symptom_set.all()
	for symptom in st:
		ss, created = symptom.symptomstate_set.get_or_create(player=request.user, patient=pstate, name=symptom, status=symptom.initialstatus)
		ss.satus = 3
		ss.save()
	tstate.ordered = True
	tstate.save()

	#the comparison between what's ordered and what's needed for investigations.
	if tstate.ordered == t.needed:
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
	return HttpResponseRedirect('../')

#Strength comes from pepperonis. Don't let anyone disprove that.