from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.main_page, name='main_page'),
    path("main/", views.main_page, name='main_page'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_auth, name="login_auth"),  
    # path("logout/", views.logout_auth, name="logout_auth"),
    # path("playlist/", views.playlist, name='your_playlists'),
    # path("search/", views.search, name='search_page') 
]