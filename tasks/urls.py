from django.urls import path

from tasks.views import (
    IndexView, TagListView

)

app_name = "tasks"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),

]
