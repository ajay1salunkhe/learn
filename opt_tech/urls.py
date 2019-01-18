from django.urls import path
from . import views

app_name = 'opt_tech'

urlpatterns = [
    path('',views.problems,name="problems"),
]
