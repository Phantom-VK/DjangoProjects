from django.urls import path
from . import views
from Register.views import TeamRegister

urlpatterns = [
path("", views.index, name = "home"),
path("about/", views.about, name = "about"),
path("contact/", views.contact, name = "contact"),
path("team_register/", TeamRegister, name = "teamRegister"),

]