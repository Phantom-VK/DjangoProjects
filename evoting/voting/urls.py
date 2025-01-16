
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('voters/', views.voter_list, name='voter_list'),
    path('voters/create/', views.voter_create, name='voter_create'),
    path('voters/<int:pk>/update/', views.voter_update, name='voter_update'),
    path('voters/<int:pk>/delete/', views.voter_delete, name='voter_delete'),
    path('candidates/', views.candidates_list, name='candi_list'),
    path('candidates/create/', views.candidate_create, name='candi_create'),
    path('candidates/<int:pk>/update/', views.candidate_update, name='candi_update'),
    path('candidates/<int:pk>/delete/', views.candidate_delete, name='candi_delete'),

]