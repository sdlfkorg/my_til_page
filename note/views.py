from django.shortcuts import render
from .models import Note, Tag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse, reverse_lazy

# Create your views here.

class NoteListView(ListView):
    model = Note
    paginate_by = 100

    def tags(self):
        return Tag.objects.all()

    def get_query_set(self):
        query_set = super(NoteListView, self).get_query_set()

        tag = self.gwargs.get('tag')
        if tag:
            query_set = query_set.filter(tag__name=tag)
        return query_set


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(CreateView):
    model = Note
    success_url = reverse_lazy('list')
    fields = ['title', 'content', 'publish']


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('list')



