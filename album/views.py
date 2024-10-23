from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from album.models import Team, Player
from django.urls import reverse_lazy

# Create your views here.
class TeamListView(ListView):
    model = Team

class PlayerListView(ListView):
    model = Player

class TeamDetailView(DetailView):
    model = Team

class PlayerDetailView(DetailView):
    model = Player

class TeamCreate(CreateView):
    model = Team
    fields = '__all__'

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class TeamUpdate(UpdateView):
    model = Team
    fields = '__all__'

class TeamDelete(DeleteView):
    model = Team
    succes_url = reverse_lazy('team-list')

class PlayerUpdate(UpdateView):
    model = Player
    fields = '__all__'

class PlayerDelete(DeleteView):
    model = Player
    succes_url = reverse_lazy('player-list')