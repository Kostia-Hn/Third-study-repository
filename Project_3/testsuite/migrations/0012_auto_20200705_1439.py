# Generated by Django 3.0.5 on 2020-07-05 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testsuite', '0011_auto_20200705_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testresult',
            old_name='score',
            new_name='avg_score',
        ),
        migrations.RemoveField(
            model_name='testresult',
            name='state',
        ),
    ]
