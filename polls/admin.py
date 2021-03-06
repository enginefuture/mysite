from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3
    

class QuestionAdmin(admin.ModelAdmin):
    '''
        Admin View for QuestionAdmin'''
    fieldsets = [
    	('Question information',{'fields':['question_text']}),
    	('Date information',	{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]




admin.site.register(Question,QuestionAdmin)
