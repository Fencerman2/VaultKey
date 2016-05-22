from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Player

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'player/index.html'
    context_object_name = 'player_list'

    def get_queryset(self):
        """Return the list of players"""
        return Player.objects.order_by('player_lastname')

class DetailView(generic.DetailView):

    model = Player

    template_name = 'player/detail.html'
