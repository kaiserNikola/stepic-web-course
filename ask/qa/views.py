from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404 
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.contrib.auth import login, logout

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
	try:
		limit=int(request.GET.get('limit', 10))
	except ValueError:
		limit=10
	if limit > 100:
		limit = 10
	try:
		page = int(request.GET.get('page', 1))
	except ValueError:
		raise Http404
	paginator = Paginator(qs, limit)
	try:
		page = paginator.page(page)
	except EmptyPage:
		page = paginator.page(paginator.num_pages)
	return page

def recent_questions(request):
	qs = Question.objects.all().order_by('-id')
	page = paginate(request, qs)
	return render(request, 'qa/questions.html', {
		'page': page,
		'title': 'Последние вопросы'
	})

def popular_questions(request):
	qs = Question.objects.order_by('-rating').all()
	page = paginate(request, qs)
	return render(request, 'qa/questions.html', {
		'page': page,
		'title': 'Популярные вопросы'
	})

def question(request, id):
	try:
		q = Question.objects.get(id=int(id))
	except Question.DoesNotExist:
		raise Http404	
	return render(request, 'qa/question.html', {
		'q': q,
		'form': AnswerForm(initial={'question': q.pk})
	})
	
def ask_form(request):
	if request.method == 'POST':
		form = AskForm(request.POST)
		form._user = request.user
		if form.is_valid():
			q = form.save()
			return redirect(q.get_absolute_url())			
	else:
		form = AskForm()	
	return render(request, 'qa/ask.html', {
		'form': form
	})	
	
def answer_form(request):
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		form._user = request.user
		if form.is_valid():
			answer = form.save()
			return redirect(answer.question.get_absolute_url())			
	return render(request, 'qa/question.html', {
		'form': form
	})			



def signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.backend = 'django.contrib.auth.backends.ModelBackend'
			login(request, user)
			return redirect('recent')	
	else:		
		form = SignupForm()			
	return render(request, 'qa/signup.html', {
		'form': form
	})			

def login_user(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			login(request, form.user)
			return redirect('recent')	
	else:		
		form = LoginForm()	
		if request.user.is_authenticated():
			print('logout')
			logout(request)				
	return render(request, 'qa/signup.html', {
		'form': form
	})	