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
    # ===================  Clinic  ======================
    # ------------------------------- Products ----------
    path("users/<int:id>/product/create/", views.create_product),
    path("users/<int:id>/product/", views.ProductListView.as_view()),
    # ------------------------------- Animals ----------
    path("users/<int:id>/animal/create/", views.create_animal),
    path("users/<int:id>/animal/", views.AnimalListView.as_view()),
    # ===================  Normal User  ======================
    path("users/<int:id>/appointment/create/", views.create_appointment),
    path(
        "users/<int:id>/appointment/", views.AppointmentListView.as_view()
    ),  # for both clinic and normal users
]
