from django.conf.urls import url
from . import views

#URLConf
urlpatterns = [
    url('home/', views.home),
    url('welcome/', views.welcome_user),
    url('logout/', views.logout)
]