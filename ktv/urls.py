from django.urls import path
from . import views

urlpatterns = [
    path('rooms/', views.room_list, name='room_list'),
    path('book-room/<int:room_id>/', views.book_room, name='book_room'),
    path('songs/', views.song_list, name='song_list'),
]
