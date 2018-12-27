from django.urls import path
from django.conf.urls import url
from . import views
import login.urls

urlpatterns = [
    path('',views.home,name="home"),
]
