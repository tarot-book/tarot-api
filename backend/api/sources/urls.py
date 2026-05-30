from django.urls import path

from .views import SourceDetailView, SourceListView

urlpatterns = [
    path("sources", SourceListView.as_view(), name="source-list"),
    path("sources/<int:pk>", SourceDetailView.as_view(), name="source-detail"),
]
