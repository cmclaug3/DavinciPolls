# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.utils.encoding import python_2_unicode_compatible


RESPONSE_CHOICES = (
		(1, 'Answer 1'),
		(2, 'Answer 2'),
		(3, 'Answer 3'),
		(4, 'Answer 4'),
	)

@python_2_unicode_compatible
class Poll(models.Model):
	name = models.CharField(max_length=250)
	answer_1 = models.CharField(max_length=250)
	answer_2 = models.CharField(max_length=250)
	answer_3 = models.CharField(max_length=250)
	answer_4 = models.CharField(max_length=250)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class UserResponse(models.Model):
	user_name = models.CharField(max_length=250)
	poll = models.ForeignKey(Poll)
	answer = models.IntegerField(choices=RESPONSE_CHOICES)

	def __str__(self):
		return 'Answer {} from {}'.format(self.answer, self.user_name)

