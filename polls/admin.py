from django.contrib import admin

from .models import Question, Choice


admin.site.site_header ='Polls App'
admin.site.site_title ='pollster Admin Area'
admin.site.index_title ='welcome to pollster app on'

# Register your models here.
# admin.site.register(Question)
# admin.site.register(Choice)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}),('Date Information',{'fields':['pub_date'],'classes':['collapse']}),]
    inlines=[ChoiceInline]
    
admin.site.register(Question,QuestionAdmin)