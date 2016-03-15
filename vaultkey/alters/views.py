from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from vaultkey.utils.emails import send_simple_message
from django.core.urlresolvers import reverse
from django.views import generic

import sys, traceback
from .forms import RequestForm
from .models import Request, Submit
# Create your views here.
class CreateView(generic.CreateView):

    model = Request
    template_name = 'alters/request_detail.html'
    fields = ('name_text', 'email_text', 'card_name', 'card_set', 'card_quantity',
        'alter_type', 'card_provided')

    def form_valid(self, form):
        # here we can add logic to send email
        print 'GOT TO form_valid'
        subject_text = "New alter request for " + form.cleaned_data['name_text']
        email_text = form.cleaned_data['email_text']
        message_text = "Check the admin site for details"
        try:
            send_simple_message(subject_text, message_text, email_text,
                ['vaultkeystudios@gmail.com'])
        except:
            print sys.exc_info(), traceback.format_exc()
        return super(CreateView, self).form_valid(form)


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

    template_name = 'alters/submit.html'
