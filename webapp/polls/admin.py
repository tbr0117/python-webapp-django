from django.contrib import admin

from .models import Choice, Question
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['QuestionId', 'QuestionText']}),
        ('Date information', {'fields': ['PostedOn']}),
    ]
    inlines = [ChoiceInline]
    search_fields = ["QuestionText"]
    list_display = ('QuestionText', 'PostedOn', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)