from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView
from django.views.generic.base import View

from .models import Test, Question


class TestList(ListView):
    model = Test
    template_name = 'test_list.html'
    context_object_name = 'test_list'
    paginate_by = 20


class TestRunView(View):
    def get(self, request, pk, seq_nr):
        try:
            question = Question.objects.filter(test_id=pk, number=seq_nr).first()
            answers = [
                answer.text
                for answer in question.answers.all()
            ]
            return \
                render(
                request=request,
                template_name='testrun.html',
                context={'question': question,
                         'answers': answers}
            )
        except:
            test = Test.objects.get(id=pk)
            return render(
                request=request,
                template_name='test_finished.html',
                context={'test': test,})

    def post(self, request, pk, seq_nr):
        data = request.POST
        text =  'you picked '
        switch = 1

        question = Question.objects.filter(test_id=pk, number=seq_nr).first()
        answers = [
            answer.text
            for answer in question.answers.all()
        ]
        quantity_of_answers = len(answers)

        for i in range(1, quantity_of_answers+1, 1):

            if data.get(str(i)) == '1':
                text += f'answer {i} '
                switch = 2

        if switch == 2:
            messages.add_message(self.request, messages.INFO, text)
        else:
            messages.add_message(self.request, messages.WARNING, 'You have to select an answer')
            return HttpResponseRedirect(self.request.path_info)

        current_question = int(self.request.path_info[-1])
        next_question = current_question + 1
        next_link = self.request.path_info [:-1] + str(next_question)

        return HttpResponseRedirect(next_link)



class TestPreView(View):

    def get(self, request, id):
        test = Test.objects.get(id=id)
        test_length = len(test.questions.all())

        return render(
            request=request,
            template_name='testpreview.html',
            context={'test': test,
                     'length': test_length}
        )

    def post(self, request):
        pass
