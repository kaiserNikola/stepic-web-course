from django.contrib import admin
from qa.models import Question, Answer

@admin.register(Question)
class QAdmin(admin.ModelAdmin):
	list_display = ('title', 'rating', 'added_at')
	

@admin.register(Answer)
class AAdmin(admin.ModelAdmin):
	pass	