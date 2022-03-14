from django.urls import path
from .views import PostView, RoomCreateView, RoomUpdateView,RoomDeleteView
from main import views

urlpatterns = [
    path('', views.index, name='main'),
    path('rules', views.rules, name='rules'),
    path('map', views.SearchView.as_view(), name='map'),
    path('<int:pk>/', PostView.as_view(), name='room_details'),
    path("room/new", RoomCreateView.as_view(), name="room_create"),
    path("room/<int:pk>/edit", RoomUpdateView.as_view(), name="room_edit"),
    path("room/<int:pk>/delete", RoomDeleteView.as_view(), name="room_delete"),
    path('MyRooms', views.MyRooms, name='MyRooms'),
]