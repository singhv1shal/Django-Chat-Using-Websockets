from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('create_room/', views.create_room, name='create_room'),
    path('join_room/', views.join_room, name='join_room'),
    path('delete_room/', views.delete_room, name='delete_room'),
    path('go_to_home/', views.go_to_home, name='go_to_home'),
    path('pending_request/', views.pending_request, name='pending_request'),
    path('approve_request/', views.approve_request, name='approve_request'),
]
