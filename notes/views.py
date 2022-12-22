from django.shortcuts import render
from rest_framework import generics
from notes.serializers import NoteSerialzer
from notes.models import Note
# Create your views here.


class ListAllNotes(generics.ListCreateAPIView):
    serializer_class = NoteSerialzer
    queryset = Note.objects.all()


class RetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerialzer
    queryset = Note.objects.all()
    lookup_field = "slug"
