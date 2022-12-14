from django.conf.urls import url
from . import views

#URLConf
urlpatterns = [
    url('welcome/', views.welcome_user)
]