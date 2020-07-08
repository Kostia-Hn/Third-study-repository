from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Count, Sum


class Topic(models.Model):

    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'


class Test(models.Model):
    LEVEL_CHOICES = (
        (1, 'Basic'),
        (2, 'Middle'),
        (3, 'Advanced'),
    )
    MIN_LIMIT = 3
    MAX_LIMIT = 20

    topic = models.ForeignKey(to=Topic, related_name='tests', null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=64)
    description = models.TextField(max_length=1024, null=True, blank=True)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES, default=2)
    image = models.ImageField(default='default.png', upload_to='covers')

    def __str__(self):
        return f'{self.title}'

    def last_run(self):
        last_run = self.test_results.order_by('-id').first()
        if last_run:
            return last_run.datetime_run
        return ''


class Question(models.Model):
    MIN_LIMIT = 3
    MAX_LIMIT = 6

    test = models.ForeignKey(to=Test, related_name='questions', on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(MAX_LIMIT)], null=True)
    text = models.CharField(max_length=64)
    description = models.TextField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f'{self.text}'

    def next(self):
        return 'next'

    def prev(self):
        return 'prev'


class Answer(models.Model):
    text = models.CharField(max_length=64)
    question = models.ForeignKey(to=Question, related_name='answers', on_delete=models.CASCADE)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.text} - {self.is_correct}'


# class TestResult(models.Model):
#     user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='test_results', on_delete=models.CASCADE)
#     test = models.ForeignKey(to=Test, related_name='test_results', on_delete=models.CASCADE)
#     avg_score = models.DecimalField(decimal_places=2, max_digits=6)
#
#
# class TestResultDetails(models.Model):
#     test_results = models.ForeignKey(to=TestResult, related_name='test_results_details', on_delete=models.CASCADE)
#     given_answers = models.ForeignKey(to=Answer, related_name='answer_details', on_delete=models.CASCADE)
#     answered_questions = models.ForeignKey(to=Question, related_name='question_details', on_delete=models.CASCADE)
#     is_correct = models.BooleanField(default=False)


class TestResult(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='test_results', on_delete=models.CASCADE)
    test = models.ForeignKey(to=Test, related_name='test_results', on_delete=models.CASCADE, null=True)

    datetime_run = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)


    current_progress = models.PositiveSmallIntegerField(default=1)
    number_of_completed_runs = models.PositiveSmallIntegerField(default=0)

    avg_score = models.DecimalField(default=0.0,
                                    validators=[MinValueValidator(0),
                                                MaxValueValidator(100)],
                                    decimal_places=2, max_digits=6)


    def update_score(self):
        qs = self.test_result_details.values('question').annotate(
            num_answers=Count('question'),
            score=Sum('is_correct')
        )
        self.avg_score = sum(
            int(entry['score']) / entry['num_answers']
            for entry in qs
        )


    def finish(self):
        self.update_score()
        self.is_completed = True
        self.number_of_completed_runs += 1

    # def __str__(self):
    #     return f'{self.test.title}, {self.user.full_name()}, {self.datetime_run}'


class TestResultDetails(models.Model):
    test_result = models.ForeignKey(to=TestResult, related_name='test_result_details', on_delete=models.CASCADE, null=True)
    question = models.ForeignKey(to=Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(to=Answer, on_delete=models.CASCADE, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'Test run: {self.test_result.id}, Question: {self.question.text}, Success: {self.is_correct}'


# class BestResults(models.Model):
#     user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='best_results', on_delete=models.CASCADE)
#     test = models.ForeignKey(to=Test, related_name='best_results', on_delete=models.CASCADE, null=True)
#
#     best_result = models.DecimalField(default=0.0, decimal_places=2, max_digits=6)