from django.urls import path, include
from introapp import views


urlpatterns = [
    path("", views.display_info, name="display_info"),
]