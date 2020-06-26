from django.contrib import admin
from .models import Test, Question, Answer


# Register your models here.

class QuestionsInline(admin.TabularInline):
    model = Question
    fields = ('text',)  # 'num_variant_min_limit')
    show_change_link = True
    extra = 1
#
#
class TestAdminModel(admin.ModelAdmin):
    fields = ('title', 'description', 'level', 'image')
    list_display = ('title', 'description', 'level', 'image')
    list_per_page = 10
    inlines = (QuestionsInline,)


class AnswersInline(admin.TabularInline):
    model = Answer
    fields = ('text', 'is_correct')  # 'num_variant_min_limit')
    show_change_link = True
    extra = 1


class QuestionAdminModel(admin.ModelAdmin):
    fields = ('text',)
    list_display = ('text',)
    list_per_page = 10
    inlines = (AnswersInline,)


admin.site.register(Test, TestAdminModel)
admin.site.register(Question, QuestionAdminModel)
