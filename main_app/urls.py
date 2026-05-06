from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro_page),
    path("user/sign_up", views.signUpCreateView.as_view()),
    path("user/sign_in", views.signInCreateView.as_view()),
    #
]
