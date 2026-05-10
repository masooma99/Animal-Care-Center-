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
    path("users/<int:id>/product/<int:product_id>/", views.productDetailView.as_view()),
    # ------------------------------- Animals ----------
    path("users/<int:id>/animal/create/", views.create_animal),
    path("users/<int:id>/animal/", views.AnimalListView.as_view()),
    path("users/<int:id>/animal/<int:animal_id>/", views.AnimalDetailView.as_view()),
    path("users/<int:id>/animal/<int:animal_id>/adopt/", views.adopt_animal),
    # ===================  Normal User  ======================
    path("users/<int:id>/appointment/create/", views.create_appointment),
    path(
        "users/<int:id>/appointment/", views.ClinicAppointmentListView.as_view()
    ),  # for both clinic and normal users
    path("users/<int:id>/appointments/", views.AppointmentListView.as_view()),
    path("users/<int:id>/pet/", views.PetListView.as_view()),
    path("users/<int:id>/order/", views.OrderListView.as_view()),
]
