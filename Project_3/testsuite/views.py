import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Test, Question, TestResult, TestResultDetails


class TestList(ListView):
    model = Test
    template_name = 'test_list.html'
    context_object_name = 'test_list'
    paginate_by = 20


class TestRunView(View):
    PREFIX = 'answer_'
    def get(self, request, pk, seq_nr):
        question = Question.objects.filter(test_id=pk, number=seq_nr).first()
        answers = [
            answer.text
            for answer in question.answers.all()
        ]
        return render(
            request=request,
            template_name='test_run.html',
            context={'question': question,
                     'answers': answers,
                     'prefix': self.PREFIX}
        )

    def post(self, request, pk, seq_nr):
        test = Test.objects.get(pk=pk)
        question = Question.objects.filter(test_id=pk, number=seq_nr).first()
        answers = [answer for answer in question.answers.all()]

        choices = {
            k.replace(self.PREFIX, ''): True
            for k in request.POST if k.startswith(self.PREFIX)
        }

        if not choices:
            messages.add_message(self.request, messages.WARNING, 'You have to select an answer')
            return HttpResponseRedirect(self.request.path_info)

        current_test_result = TestResult.objects.filter(
            test=test,
            user=request.user,
            is_completed=False).last()

        for idx, answer in enumerate(answers, 1):
            value = choices.get(str(idx), False)
            test_result_detail = TestResultDetails.objects.create(
                test_result=current_test_result,
                question=question,
                answer=answer,
                is_correct=(value == answer.is_correct)
            )

        messages.add_message(self.request, messages.INFO, choices)
        if question.number < test.questions.count():
            return redirect(reverse('test:testrun_step', kwargs={'pk': pk, 'seq_nr': seq_nr + 1}))
        else:
            current_test_result.finish()

            current_test_result.save()
            return render(
                request=request,
                template_name='test_finished.html',
                context={'test_result': current_test_result,
                         'time_spent': datetime.datetime.utcnow() - current_test_result.datetime_run.replace(tzinfo=None)})


class TestPreView(View):

    def get(self, request, id):
        test = Test.objects.get(id=id)
        test_result = TestResult.objects.create(
            user=request.user,
            test=test
        )

        test_length = test.questions.count()  #len(test.questions.all())

        return render(
            request=request,
            template_name='testpreview.html',
            context={'test': test,
                     'length': test_length,
                     'test_result': test_result}
        )

    def post(self, request):
        pass
