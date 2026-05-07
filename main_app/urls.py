from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro_page),
    path("auth/sign-up", views.SignUpView.as_view()),
    #
]
