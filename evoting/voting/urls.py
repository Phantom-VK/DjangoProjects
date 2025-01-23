
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Voter URLS
    path('voters/', views.voter_list, name='voter_list'),
    path('voters/create/', views.voter_create, name='voter_create'),
    path('voters/<int:pk>/update/', views.voter_update, name='voter_update'),
    path('voters/<int:pk>/delete/', views.voter_delete, name='voter_delete'),
    # Candicates URL
    path('candidates/', views.candidates_list, name='candi_list'),
    path('candidates/create/', views.candidate_create, name='candi_create'),
    path('candidates/<int:pk>/update/', views.candidate_update, name='candi_update'),
    path('candidates/<int:pk>/delete/', views.candidate_delete, name='candi_delete'),

    # Campaign URLs
    path('campaigns/', views.campaign_list, name='campaign_list'),
    path('campaigns/create/', views.campaign_create, name='campaign_create'),
    path('campaigns/<int:pk>/update/', views.campaign_update, name='campaign_update'),
    path('campaigns/<int:pk>/delete/', views.campaign_delete, name='campaign_delete'),

    # Results and Voting
    path('results/', views.result_list, name='result_list'),
    path('vote/', views.cast_vote, name='cast_vote'),
]