from django.shortcuts import render

from django.http import HttpResponseRedirect

# Create your views here.

from .models import *


def index(request):
	k=Song.objects.all()[0]
	k=str(k)
	context={'song':k}
	print(k)
	return render(request, 'music/search.html', context)
def search(request):
	form={}
	artist=[]
	album=[]
	song_t=[]
	audio_u=[]
	if request.method == 'POST':
		song_title=request.POST['search']
		album_name=request.POST['search']
		artist_name=request.POST['search']
		if(len(Album.objects.filter(album_name=album_name))>0):
			a=Album.objects.get(album_name=album_name)
		else:
			a=0
		if(len(Artist.objects.filter(artist_name=artist_name))>0):
			b=Artist.objects.get(artist_name=artist_name)
		else:
			b=0
		if(a):
			for i in range(a.song_set.count()):
				song_data=a.song_set.all()[i]
				song_data=str(song_data)
				song_data=song_data.split(',')
				artist.append(song_data[0])
				album.append(song_data[1])
				song_t.append(song_data[2])
				audio_u.append(song_data[3])
		elif(b):
			for j in range(b.album_set.count()):
				c=b.album_set.all()[j]
				print(c)
				print('hello')
				for i in range(c.song_set.count()):
					song_data=c.song_set.all()[i]
					song_data=str(song_data)
					print(song_data)
					song_data=song_data.split(',')
					artist.append(song_data[0])
					album.append(song_data[1])
					song_t.append(song_data[2])
					audio_u.append(song_data[3])
			
			
		else:
			return HttpResponseRedirect('/')
	mylist = zip(artist,album,song_t,audio_u)
	context = {
            'mylist': mylist,
        }
	#context={'artist':artist,'album':album,'song_title':song_t,'audio_url':audio_u}
	return render(request, 'music/index2.html', context)
			
def songsview(request):
	artist=[]
	album=[]
	song_t=[]
	audio_u=[]	
	for i in range(Song.objects.count()):
		song_data=Song.objects.all()[i]
		song_data=str(song_data)
		print(song_data)
		song_data=song_data.split(',')
		artist.append(song_data[0])
		album.append(song_data[1])
		song_t.append(song_data[2])
		audio_u.append(song_data[3])
	mylist = zip(artist,album,song_t,audio_u)
	context = {
            'mylist': mylist,
        }
	#context={'artist':artist,'album':album,'song_title':song_t,'audio_url':audio_u}
	return render(request, 'music/index2.html', context)		
				
				
				
	
