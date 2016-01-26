from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .forms import RequestForm
from .models import Request, Submit
# Create your views here.
class CreateView(generic.CreateView):

    model = Request
    template_name = 'requests/request_detail.html'
    fields = ('name_text', 'email_text', 'card_name', 'card_set', 'card_quantity',
        'alter_type', 'card_provided')


    # def get_form(self, request):
    #     if self.request.method == 'POST':
    #         form = RequestForm(request.POST)
    #         if form.is_valid():
    #             return render (request, 'requests/submit.html')
    #     else:
    #         form = RequestForm()
    #
    #     return render(request, 'requests/request_detail.html', {'form': form})


class SubmitView(generic.DetailView):

    model = Request

    template_name = 'requests/submit.html'
