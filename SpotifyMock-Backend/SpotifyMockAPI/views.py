from django.shortcuts import render
from rest_framework import generics
from .models import Album, SongDetails, Song, Genre, Artist, Playlist, Library
from .serializers import  (AlbumSerializer, 
                            SongDetailSerializer, 
                            SongSerializer,
                            GenreSerializer,
                            ArtistSerializer,
                            PlaylistSerializer,
                            LibrarySerializer
                            )

# Create your views here.
class GenreView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AlbumView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer

    def get_queryset(self):
        album_id = self.kwargs.get('pk')
        album = Album.objects.get(pk=album_id)
        return Album.objects.filter(pk=album.pk)

class SongView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = SongDetailSerializer

    def get_queryset(self):
        song_id = self.kwargs.get('pk')
        song = Song.objects.get(pk=song_id)
        return SongDetails.objects.filter(pk=song.song_details.pk)