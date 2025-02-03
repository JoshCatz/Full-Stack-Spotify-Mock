from rest_framework import serializers
from .models import Song, SongDetails, Album, Genre, Artist, Playlist, Library
from rest_framework.reverse import reverse

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['title']


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['pfp', 'label']

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    songs = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='song-details'
    )

    class Meta:
        model = Album
        fields = ['id', 'title', 'artist', 'songs', 'genre']

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