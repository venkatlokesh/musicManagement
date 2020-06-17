from django.urls import path

from . import views
from django.conf.urls import url, include
urlpatterns = [
  
    path(r'', views.index, name='index'),
	path(r'searchpage/',views.index2,name='index2'),
	path(r'delete/<path:a_url>/', views.deletesong ,name = "deletesong") ,
	path(r'play/<path:a_url>/', views.playsong ,name = "playsong") ,
	path(r'songupload/',views.index3,name='index3'),
	url(r'/search/', views.search , name = "search"),
	url(r'/add/', views.add , name = "add"),
	path(r'songs/',views.songsview, name="songs"),]