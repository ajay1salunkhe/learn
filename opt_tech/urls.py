from django.urls import path
from . import views

app_name = 'opt_tech'

urlpatterns = [
    path('',views.problems,name="problems"),
    path('assignment-problem',views.ass_problem,name="ass_problem"),
    path('assignment-problem/answer',views.ass_problem_ans,name="ass_problem_ans"),
]
