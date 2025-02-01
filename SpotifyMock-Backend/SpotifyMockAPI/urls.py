from django.urls import path
from . import views

urlpatterns = [
    path('album/', views.AlbumView.as_view(), name='album'),
    path('album/<int:pk>', views.AlbumDetailView.as_view(), name='album-detail'),
    path('songs/', views.SongView.as_view(), name='song'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song-details')
]
