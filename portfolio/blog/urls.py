from django.urls import path
from .views import (
    HomePageView,
    DetailPageView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("post/<int:pk>/", DetailPageView.as_view(), name="details"),
    path("post/new/", BlogCreateView.as_view(), name="create"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="update"),
    path(
        "post/<int:pk>/delete/",
        BlogDeleteView.as_view(),
        name="delete",
    ),
]
