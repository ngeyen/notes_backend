from notes.models import Note
from notes.serializers import NoteSerialzer
from rest_framework import generics
from notes import views
from django.urls import re_path

urlpatterns = [
    re_path(r"^$", views.ListAllNotes.as_view(), name="all-notes"),
    re_path(r"^(?P<slug>[\w\-]+)/$",
            views.RetrieveUpdateDelete.as_view(), name="get-note"),

]


# Create your views here.
