from django.urls import path
from django.conf.urls import url
from . import views
import login.urls

urlpatterns = [
    path('',views.home,name="home"),
    path('aboutus/',views.aboutus,name="aboutus"),
    path('categories/',views.categories,name="categories"),
    path('categories/tutorials/',views.tutorials,name="tutorials"),
]
