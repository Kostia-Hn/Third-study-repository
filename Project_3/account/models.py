from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from testsuite.models import TestResult


class ProUser(AbstractUser):
    image = models.ImageField(default='default.jpg', upload_to='pics', null=True, blank=True)
    avr_score = models.IntegerField(null=True, blank=True)
    rank = models.IntegerField(default=50, null=True, blank=True)
    points = models.IntegerField(default=100, null=True, blank=True)

    def determine_unfinished_tests(self, test):
        qs = TestResult.objects.filter(user=self.id, test=test, is_completed=False)
        if len(qs)>0:
            message = f'you have {len(qs)} unfinished tests'
            list = [message, qs]
            return list
        else:
            return False

    def number_of_runs(self, test):
        qs = TestResult.objects.filter(user=self.id, test=test)
        return len(qs)

    def best_result(self, test):
        qs = TestResult.objects.filter(user=self.id, test=test)
        best_result = 0
        for i in qs:
            if i.avg_score > best_result:
                best_result = i.avg_score

        return best_result

    def total_number_of_runs(self):
        qs = TestResult.objects.filter(user=self.id)
        return len(qs)

    def last_run(self):
        qs = TestResult.objects.filter(user=self.id)

        if len(qs) == 1:
            last_run = qs[0].datetime_run

        elif len(qs) > 1:
            last_run = qs[0].datetime_run
            for i in qs:
                if i.datetime_run > last_run:
                    last_run = i.datetime_run
        else:
            last_run = 'Never'

        return last_run

    def total_score(self):
        qs = TestResult.objects.filter(user=self.id)
        total_score = 0
        for i in qs:
            total_score += i.avg_score

        return total_score

    # def success_rate(self):
    #     qs = TestResult.objects.filter(user=self.id)
    #     success_rate = 0
    #
    #     total_score = 0
    #     for i in qs:
    #         i.avg_score += total_score
    #
    #     max_possible_score = 0
    #     for i in qs:
    #         i.test.q
