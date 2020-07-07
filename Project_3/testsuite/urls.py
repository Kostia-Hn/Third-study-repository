from django.urls import path

from .views import TestList, TestRunView, TestPreView

app_name = 'test'

urlpatterns = [

    path('list/', TestList.as_view(template_name='test_list.html'), name='list'),

    path('<int:pk>/question/<int:seq_nr>', TestRunView.as_view(), name='testrun_step'),

    path('<int:id>/', TestPreView.as_view(), name='test preview'),

    # path('<int:pk>/start', StartTestView.as_view(), name='start'),
]
