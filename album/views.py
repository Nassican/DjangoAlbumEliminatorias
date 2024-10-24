from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from album.models import Team, Player
from django.urls import reverse_lazy
from django.contrib import messages

# Create your views here.
class TeamListView(ListView):
    model = Team

class PlayerListView(ListView):
    model = Player

class TeamDetailView(DetailView):
    model = Team

class PlayerDetailView(DetailView):
    model = Player
    
class TeamCreateView(CreateView):
    model = Team
    fields = '__all__'


class PlayerCreateView(CreateView):
    model = Player
    fields = '__all__'

class TeamUpdateView(UpdateView):
    model = Team
    fields = '__all__'
    template_name = 'album/team_form.html'

class PlayerUpdateView(UpdateView):
    model = Player
    fields = '__all__'
    template_name = 'album/player_form.html'


class TeamDeleteView(DeleteView):
    model = Team
    success_url = reverse_lazy('team-list')
    
    def delete(self, request, *args, **kwargs):
        team = self.get_object()
        messages.success(request, f'El equipo "{team.name}" ha sido eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

class PlayerDeleteView(DeleteView):
    model = Player
    success_url = reverse_lazy('player-list')
    
    def delete(self, request, *args, **kwargs):
        player = self.get_object()
        messages.success(request, f'El jugador "{player.first_name} {player.last_name}" ha sido eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)

class HomeView(TemplateView):
    template_name = 'base.html'
