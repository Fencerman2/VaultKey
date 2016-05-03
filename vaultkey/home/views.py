from django.shortcuts import render, render_to_response
from articles.models import Article
from player.models import Player

# Create your views here.
def index(request):
    return render_to_response('home/index.html',
        {'recent_articles': Article.objects.order_by('-pub_date')[:6],
        'player_list':     Player.objects.order_by('player_lastname')
        }
    )
