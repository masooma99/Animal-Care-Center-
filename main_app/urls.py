from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro_page),
    path("auth/sign-up", views.SignUpView.as_view()),
    # -------------------------------user ----------
    path("users/<int:id>/", views.UserDetailView.as_view()),
    path("users/", views.UserListView.as_view()),
]
