from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.PostView.as_view()),
    path(r"<int:pk>/", views.DeletePostView.as_view()),
]
