"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from qa import views

urlpatterns = [
    url(r'^$', views.recent_questions, name='recent'),
    url(r'^login/', views.login_user),
    url(r'^signup/', views.signup),
    url(r'^question/(?P<id>[^/]+)/', views.question, name='question'),
    url(r'^ask/', views.ask_form),
    url(r'^answer/', views.answer_form),
    url(r'^popular/', views.popular_questions),
    url(r'^new/', views.test),
    url(r'^admin/', admin.site.urls),
]
