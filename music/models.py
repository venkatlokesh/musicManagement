from django.db import models
import datetime
# Create your models her
from django.contrib.auth import get_user_model
from django.urls import reverse





# Create your models here.

class Artist(models.Model):
    artist_name = models.CharField(max_length=30)
    




    def __str__(self):
        return self.artist_name



    

class Album(models.Model):
    #artist = models.CharField(max_length=250)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE )
    album_name = models.CharField(max_length = 250)

    def __str__(self):
        return str(self.artist)+','+str(self.album_name)


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    
    audio_url=models.CharField(max_length=1000,help_text="Copy the url link of the song",unique="TRUE")
    
    def __str__(self):
        return str(self.album)+','+str(self.song_title)+','+str(self.audio_url)