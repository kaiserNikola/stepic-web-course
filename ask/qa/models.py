from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.urlresolvers import reverse

class Question(models.Model):
	title = models.CharField(max_length=128, verbose_name='заголовок вопроса')
	text  = models.TextField(verbose_name='полный текст вопроса', blank=True)
	added_at = models.DateTimeField(verbose_name='дата добавления вопроса', default=timezone.now)
	rating   = models.IntegerField(default=0, verbose_name='рейтинг вопроса')
	author   = models.ForeignKey(User, verbose_name='автор вопроса', related_name='questions')
	likes    = models.ManyToManyField(User, verbose_name='список пользователей, поставивших "лайк"', related_name='liked_questions', null=True, blank=True)
	
	def get_absolute_url(self):
		return reverse('question', kwargs={'id': self.pk})
		

class Answer(models.Model):
	text     = models.TextField(verbose_name='текст ответа')
	added_at = models.DateTimeField(verbose_name='дата добавления ответа', default=timezone.now)
	question = models.ForeignKey(Question, verbose_name = 'вопрос, к которому относится ответ')
	author   = models.ForeignKey(User, verbose_name='автор ответа.')
	
	#def get_absolute_url(self):
	#	return reverse('answer', kwargs={'id': self.pk})
	
	class Meta:
		ordering = ['-added_at'] 

