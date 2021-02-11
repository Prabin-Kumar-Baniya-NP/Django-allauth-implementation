from django.urls import path
from . import views
app_name = "google_auth"
urlpatterns = [
    path("", views.index, name = "index-page"),
]
