from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Test

class TestList(ListView):
    model = Test
    template_name = 'test_list.html'
    context_object_name = 'test_list'
    paginate_by = 20