from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Song, SongDetails, Album, Genre, Artist, Playlist, Library
from rest_framework.reverse import reverse

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title']

class ArtistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Artist
        fields = ['user', 'pfp', 'label']

    def create(self, validated_data):
        user_data = validated_data.pop("user")
        formatted_username = user_data['username'].replace(' ', '_')

        user = User.objects.create_user(
            username=formatted_username,
            email=user_data['email'],
            password=user_data['password']
        )

        artist = Artist.objects.create(user=user, **validated_data)
        return artist

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    artist = ArtistSerializer(read_only=True)
    songs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song-details'
    )

    class Meta:
        model = Album
        fields = ['id', 'title', 'songs', 'artist']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['artist'] = {
            'name':instance.artist.name
        }

        return representation

class SongDetailSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.SerializerMethodField()
    artist = serializers.SerializerMethodField()
    album = serializers.SerializerMethodField()
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='title'
    )
    class Meta:
        model = SongDetails
        fields = ['title', 'album', 'artist', 'duration', 'lyrics', 'genre']

    def get_title(self, obj):
        song = obj.songs.first()
        if song:
            return song.title
        return None
    
    def get_artist(self, obj):
        song = obj.songs.first()
        if song:
            return song.artist
        return None
    
    def get_album(self, obj):
        song = obj.songs.first()
        if song:
            request = self.context.get('request')
            return reverse('album-detail', kwargs={'pk': song.album.id}, request=request)
        return None

class SongSerializer(serializers.ModelSerializer):
    song_details = SongDetailSerializer()
    album = serializers.HyperlinkedRelatedField(
        queryset=Album.objects.all(),
        view_name='album-detail'
    )
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'song_details']

    def create(self, validated_data):
        song_details_data = validated_data.pop("song_details")
        song_details_instance = SongDetails.objects.create(**song_details_data)

        song_instance = Song.objects.create(song_details=song_details_instance, **validated_data)

        return song_instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        song_details = instance.song_details

        if song_details:
            representation['song_details'] = reverse(
                'song-details',
                kwargs={'pk': song_details.pk},
                request=self.context.get('request')
            )

        return representation
    
class PlaylistSerializer(serializers.ModelSerializer):
    songs = serializers.RelatedField(queryset=Song.objects.all())
    class Meta:
        model = Playlist
        fields = ['title', 'description', 'public', 'songs']

class LibrarySerializer(serializers.ModelSerializer):
    playlists = serializers.RelatedField(queryset=Song.objects.all())
    class Meta:
        model = Library
        fields = ['playlists']

