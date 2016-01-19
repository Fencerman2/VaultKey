from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Article

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'cards/index.html'
    context_object_name = 'latest_article_list'

    def get_queryset(self):
        """Return the last five published articles."""
        return Article.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):

    model = Article

    template_name = 'cards/detail.html'
