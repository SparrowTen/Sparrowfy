from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.main_page, name='main_page'),
    path("main/", views.main_page, name='main_page'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_auth, name="login_auth"),  
    path("signup/submit", views.signupsubmit, name="signupsubmit"),
    path("login/submit", views.loginsubmit, name='loginsubmit'),
    path("main/search", views.search, name='search_page') 
]