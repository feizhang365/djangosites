"""
Admin
"""
from django.contrib import admin

# Register your models here.

from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    """
     choice
    """
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    """
    Customize Question Admin form
    """
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
