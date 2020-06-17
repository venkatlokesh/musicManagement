from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.http import HttpResponse
# Create your views here.

from .models import *


def index(request):
	context={}
	return render(request, 'music/index.html', context)
def index2(request):
	context={}
	return render(request, 'music/search.html', context)
def index3(request):
	context={}
	return render(request, 'music/add.html', context)
def search(request):   # searching songs view
	form={}
	artist=[]
	album=[]
	song_t=[]
	audio_u=[]
	if request.method == 'POST':
		song_title=request.POST['search']
		album_name=request.POST['search']
		artist_name=request.POST['search']
		if(len(Album.objects.filter(album_name__iexact=album_name))>0):# checking for case insensitive album name
			a=Album.objects.get(album_name__iexact=album_name)
		else:
			a=0
		if(len(Artist.objects.filter(artist_name__iexact=artist_name))>0):# checking whether given input matches case insensitive artist or not
			b=Artist.objects.get(artist_name__iexact=artist_name)
		else:
			b=0
		if(len(Song.objects.filter(song_title__icontains=song_title))>0):#checking whether given input matches any case insensitive song or not
			k=Song.objects.filter(song_title__icontains=song_title)
		else:
			k=0
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
			
			
		elif(k):
				for i in range(len(k)):
					song_data=k[i]
					song_data=str(song_data)
					print(song_data)
					song_data=song_data.split(',')
					artist.append(song_data[0])
					album.append(song_data[1])
					song_t.append(song_data[2])
					audio_u.append(song_data[3])
					
		
		else:	
			return HttpResponseRedirect('/searchpage/') # if input is not artist and not an album redirecting 
	mylist = zip(artist,album,song_t,audio_u)
	context = {
            'mylist': mylist,
        }
	#context={'artist':artist,'album':album,'song_title':song_t,'audio_url':audio_u}
	return render(request, 'music/index2.html', context)
			
def songsview(request): # view function for all songs
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
def add(request):  # method for adding a song
	if request.method == 'POST':
		song_title=request.POST['song_title']
		album_name=request.POST['album_name']
		artist_name=request.POST['artist_name']
		audio_url=request.POST['audio_url']
		#audio_url=audio_url.replace('?','}')
		if(len(Artist.objects.filter(artist_name__iexact=artist_name))==0): #checking whether input artist with incase sensitive  already exits or not if not create one artist
			artist=Artist()
			artist.artist_name=artist_name
			artist.save()
		artist=Artist.objects.get(artist_name__iexact=artist_name)	
		if(len(artist.album_set.filter(album_name__iexact=album_name))==0):#checking whether input album with incase sensitive already exits or not if not create one album
			
			artist.album_set.create(album_name=album_name)
		album=artist.album_set.get(album_name__iexact=album_name)
		album.song_set.create(song_title=song_title ,audio_url=audio_url) # adding a song to reqiured album
		#album.song_set.create(audio_url=audio_url)
		context={'value':0}
		return HttpResponseRedirect('/songs/') # after adding we can see added song

		
def deletesong(request,a_url):  # method for deleting a song
	song=Song.objects.get(audio_url=a_url)
	song.delete()
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
def playsong(request,a_url):  # method for playing a song
	print(a_url)
	song=Song.objects.get(audio_url=a_url)
	a_url=song.audio_url
	#audio_url=a_url.replace('}','?')
	#print(audio_url)
	#https://music.apple.com/in/album/hes-soo-cute-from-sarileru-neekevvaru/1491738278?i=1491738282
	context={'a_url':a_url}
	return render(request,'music/play.html',context)

					
		
		
				
				
				
	
