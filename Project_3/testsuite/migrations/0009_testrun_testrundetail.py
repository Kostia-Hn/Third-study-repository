# Generated by Django 3.0.5 on 2020-07-05 11:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testsuite', '0008_auto_20200628_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_run', models.DateTimeField(auto_now_add=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('score', models.PositiveSmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('state', models.PositiveSmallIntegerField(choices=[(1, 'New'), (2, 'Started')], default=1)),
                ('test_suite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_suite_runs', to='testsuite.Test')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_suite_runs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TestRunDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='testsuite.Answer')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testsuite.Question')),
                ('test_suite_run', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='testsuite.TestRun')),
            ],
        ),
    ]
