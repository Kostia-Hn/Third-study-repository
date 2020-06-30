from django.contrib import admin
from .models import Test, Question, Answer
from .forms import TestForm, QuestionsInlineFormSet, QuestionsInlineForm, AnswerInlineFormSet


# Register your models here.

class AnswersInline(admin.TabularInline):
    model = Answer
    fields = ('text', 'is_correct')
    show_change_link = True
    extra = 0
    formset = AnswerInlineFormSet


class QuestionAdminModel(admin.ModelAdmin):
    fields = ('text',)
    list_select_related = ('test',)
    list_display = ('text',)
    list_per_page = 10
    inlines = (AnswersInline,)


class QuestionsInline(admin.TabularInline):
    model = Question
    fields = ('text',)  # 'num_variant_min_limit')
    show_change_link = True
    extra = 0
    formset = QuestionsInlineFormSet
    form = QuestionsInlineForm


class TestAdminModel(admin.ModelAdmin):
    fields = ('title', 'description', 'level', 'image')
    list_display = ('title', 'description', 'level', 'image')
    list_per_page = 10
    inlines = (QuestionsInline,)
    form = TestForm




admin.site.register(Test, TestAdminModel)
admin.site.register(Question, QuestionAdminModel)
