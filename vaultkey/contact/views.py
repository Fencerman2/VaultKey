from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Contact
# Create your views here.
class CreateView(generic.CreateView):

    model = Contact
    template_name = 'contact/detail.html'
    fields = ('name_text', 'email_text', 'message_text')

class SendView(generic.DetailView):

    model = Contact

    template_name = 'contact/submit.html'
