# Generated by Django 3.0.5 on 2020-06-24 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsuite', '0003_auto_20200624_2217'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestResultDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answered_questions', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_details', to='testsuite.Question')),
                ('given_answers', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_details', to='testsuite.Answer')),
                ('test_results', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_results_d', to='testsuite.TestResult')),
            ],
        ),
    ]
