from django.db import models
from django.contrib.auth.models import User
from datetime import timezone

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pfp = models.ImageField(upload_to='artist_pfp/', null=True, blank=True)
    label = models.CharField(max_length=255, null=True)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='album')

    def __str__(self):
        return self.title
    
class SongDetails(models.Model):
    duration = models.IntegerField()
    lyrics = models.TextField(blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, related_name='genre')

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    song_details = models.ForeignKey(SongDetails, on_delete=models.CASCADE, related_name="songs")
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.deleted_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Playlist(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    public = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
    songs = models.ManyToManyField(Song, related_name='playlists')

class Library(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.PROTECT, null=True, related_name='library')
    user = models.ManyToManyField(User, related_name='library')

