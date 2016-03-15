from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User


class AskForm(forms.Form):
	title = forms.CharField()
	text  = forms.CharField()
	
	def save(self):
		user, created = User.objects.get_or_create(first_name='test')
		q = Question.objects.create(title=self.cleaned_data['title'], text=self.cleaned_data['text'], author=user)
		return q
		
		

class AnswerForm(forms.Form):
	text     = forms.CharField()
	question = forms.IntegerField(required=False)
		
	def save(self):
		user, created = User.objects.get_or_create(first_name='test')
		q = Question.objects.get(pk=int(self.cleaned_data['question']))
		a = Answer.objects.create(text=self.cleaned_data['text'], author=user, question=q)
		return a