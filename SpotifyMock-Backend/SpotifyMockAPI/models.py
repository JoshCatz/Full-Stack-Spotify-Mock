from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    genre = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
    
class SongDetails(models.Model):
    durations = models.IntegerField()
    lyrics = models.TextField(blank=True, null=True)

class Song(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    song_details = models.ForeignKey(SongDetails, on_delete=models.CASCADE, related_name="songs")

    def __str__(self):
        return self.title
