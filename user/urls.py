from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path("register", views.Register.as_view(), name="register_user"),
    path("login", views.Login.as_view(), name="login_user"),
    path("logout", views.Logout, name="logout_user"),
]
