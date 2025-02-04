from django.urls import path
from . import views

urlpatterns = [
    path('album/', views.AlbumView.as_view(), name='album'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),
    path('songs/', views.SongView.as_view(), name='song'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song-details'),
    path('genres/', views.GenreView.as_view(), name='genres'),
    path('user/signup', views.UserSignupView.as_view(), name='user-signup'),
    path('user/login', views.UserLoginView.as_view(), name='user-login'),
    path('artist/signup', views.ArtistSignupView.as_view(), name='artist-signup'),
    path('artist/login', views.ArtistLoginView.as_view(), name='artist-login'),
]
