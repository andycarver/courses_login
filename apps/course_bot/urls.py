from django.conf.urls import url
from . import views
# from django.contrib import admin

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^confirm/(?P<id>\d+)$', views.confirm),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^add_user_to_course$', views.users_courses),
    url(r'^add_user$', views.add_user),
]
