from django.urls import path

from .models import Commentary
from .views import (
    MainPageView,
    PostDetailView
)


urlpatterns = [
    path(
        "",
        MainPageView.as_view(),
        name="index"
    ),
    path(
        "post/<int:pk>",
        PostDetailView.as_view(),
        name="post-detail"
    ),
]

app_name = "blog"