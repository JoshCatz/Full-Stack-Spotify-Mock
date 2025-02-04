from django.shortcuts import render
from rest_framework import generics, status
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate

from rest_framework.permissions import IsAuthenticated
from .permissions import IsArtist

from .models import Album, SongDetails, Song, Genre, Artist, Playlist, Library
from .serializers import  (AlbumSerializer, 
                            SongDetailSerializer, 
                            SongSerializer,
                            GenreSerializer,
                            ArtistSerializer,
                            PlaylistSerializer,
                            LibrarySerializer,
                            UserSerializer
                            )

# Create your views here.
class GenreView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

# Album view for regular users

class AlbumCreateView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated]

# Album view for artist users

class AlbumListView(generics.ListAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [IsAuthenticated, IsArtist]

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
    
# User Signup/Login Views
class UserSignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


        if user is not None:
            return Response({
                'message': 'Login successful',
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid username or password'
            }, status=status.HTTP_401_UNAUTHORIZED)


# Artist Signup/Login Views
class ArtistSignupView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data

        user = User.objects.create_user(
            username=data.get('username'),
            password=data.get('password'),
            email=data.get('email'),
        )

        artist = Artist.object.create(user=user, pfp='', label='')

        return Response({'message': 'Artist registered successfully'})

class ArtistLoginView(APIView):

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)

        artist = Artist.objects.filter(user=user).first()
        if artist:
            return Response({
                'message': 'Login successful',
                'username': user.username,
                'email': user.email
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Invalid username or password'
            }, status=status.HTTP_401_UNAUTHORIZED)
        
