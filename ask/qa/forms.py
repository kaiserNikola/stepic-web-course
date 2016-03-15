from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class AskForm(forms.Form):
	title = forms.CharField()
	text  = forms.CharField()
	
	def save(self):
		try:
			user = self._user
		except Exception:	
			user, created = User.objects.get_or_create(first_name='test')
		q = Question.objects.create(title=self.cleaned_data['title'], text=self.cleaned_data['text'], author=user)
		return q
		
		

class AnswerForm(forms.Form):
	text     = forms.CharField()
	question = forms.IntegerField()
		
	def save(self):
		try:
			user = self._user
		except Exception:	
			user, created = User.objects.get_or_create(first_name='test')
		q = Question.objects.get(pk=int(self.cleaned_data['question']))
		a = Answer.objects.create(text=self.cleaned_data['text'], author=user, question=q)
		return a


class SignupForm(forms.Form):
	username = forms.CharField()
	email 	 = forms.EmailField()
	password = forms.CharField()
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError("Such user already in db!")
		return username		
	
	def save(self):
		user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email'], self.cleaned_data['password'])
		user.save()
		return authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
		
	def clean(self):
		super().clean()
		print(self.cleaned_data)
		user = authenticate(username=self.cleaned_data.get('username'), password=self.cleaned_data.get('password'))
		print(user)
		if user is not None:
			if user.is_active:
				self.user = user
				return self.cleaned_data
			else:
				raise forms.ValidationError("Your account has been disabled!")
		else:
			raise forms.ValidationError("Your username and password were incorrect.")
					
