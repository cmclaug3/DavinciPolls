from django import forms

from polls.models import UserResponse


class UserResponseForm(forms.ModelForm):
	class Meta:
		model = UserResponse
		fields = ['user_name', 'poll', 'answer',]
		