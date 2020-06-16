from django.urls import path

from . import views
from django.conf.urls import url, include
urlpatterns = [
    # ex: /polls/
    path(r'search/', views.index, name='index'),

	url(r'/add/', views.search , name = "add"),
	path(r'songs/',views.songsview, name="songs"),]