# Generated by Django 3.0.5 on 2020-07-05 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsuite', '0012_auto_20200705_1439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testresultdetails',
            name='test_suite_run',
        ),
        migrations.AddField(
            model_name='testresultdetails',
            name='test_result',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test_result_details', to='testsuite.TestResult'),
        ),
        migrations.AlterField(
            model_name='testresultdetails',
            name='answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testsuite.Answer'),
        ),
    ]
