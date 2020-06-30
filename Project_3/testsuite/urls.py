from django.urls import path
from django.views.generic import TemplateView
from .views import TestList

app_name = 'test'

urlpatterns = [

    path('start/<int:id>', TemplateView.as_view(template_name='Test_start.html'), name='test_start'),
    path('list/', TestList.as_view(template_name='test_list.html'), name='list'),

]
