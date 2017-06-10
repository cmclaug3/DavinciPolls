# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from polls.models import Poll, UserResponse
from polls.forms import UserResponseForm


def home(request):
	context = {
		'polls': Poll.objects.all()
	}
	return render(request, 'base.html', context)

def user_poll(request, poll_id):
	poll = Poll.objects.get(id=poll_id)
	msg = ''

	if request.method == 'POST':
	 	form = UserResponseForm(request.POST)
	 	if form.is_valid():
	 		form.save()
	 		msg = 'Your answer has been saved.'
	else:
		form = UserResponseForm(initial={'poll': poll})

	context = {
		'poll': poll,
		'form': form,
		'msg': msg,
		}
	return render(request, 'user_poll.html', context)
	

