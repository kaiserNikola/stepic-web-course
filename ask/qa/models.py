from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
	title = models.CharField(max_length=128, verbose_name='заголовок вопроса')
	text  = models.TextField(verbose_name='полный текст вопроса')
	added_at = models.DateTimeField(verbose_name='дата добавления вопроса', default=timezone.now)
	rating   = models.IntegerField(verbose_name='рейтинг вопроса')
	author   = models.ForeignKey(User, verbose_name='автор вопроса', related_name='questions')
	likes    = models.ManyToManyField(User, verbose_name='список пользователей, поставивших "лайк"', related_name='liked_questions')


class Answer(models.Model):
	text     = models.TextField(verbose_name='текст ответа')
	added_at = models.DateTimeField(verbose_name='дата добавления ответа', default=timezone.now)
	question = models.ForeignKey(Question, verbose_name = 'вопрос, к которому относится ответ', related_name='answers')
	author   = models.ForeignKey(User, verbose_name='автор ответа.')

