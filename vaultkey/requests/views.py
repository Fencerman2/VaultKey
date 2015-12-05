from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Request, Submit
# Create your views here.
class DetailView(generic.DetailView):

    model = Request

    template_name = 'requests/requestform.html'

class SubmitView(generic.DetailView):

    model = Submit

    template_name = 'requests/submit.html'
