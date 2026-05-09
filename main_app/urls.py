from django.urls import path
from . import views

urlpatterns = [
    path("", views.intro_page),
    # ------------------------------- auth ----------
    path("auth/sign-up", views.SignUpView.as_view()),
    # -------------------------------user profile page ----------
    path("users/<int:id>/", views.UserDetailView.as_view()),
    # ------------------------------- user details ----------
    path("users/", views.UserListView.as_view()),  # for the homepage
    # path("product/create/", views.ProductCreateView.as_view()),
    path("users/<int:id>/product/create/", views.create_product),
    path("animal/create/", views.AnimalCreateView.as_view()),
    path("users/<int:id>/product/", views.ProductListView.as_view()),
]
