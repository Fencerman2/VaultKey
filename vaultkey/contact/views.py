from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Contact

import sys, traceback
# Create your views here.
class CreateView(generic.CreateView):

    model = Contact
    template_name = 'contact/detail.html'
    fields = ('name_text', 'email_text',  'subject_text', 'message_text')

    def form_valid(self, form):
        # here we can add logic to send email
        print 'GOT TO form_valid'
        subject_text = form.cleaned_data['subject_text']
        email_text = form.cleaned_data['email_text']
        message_text = form.cleaned_data['message_text']
        try:
            send_mail(subject_text, message_text, email_text,
                ['vaultkeystudios@gmail.com'], fail_silently=False)
        except:
            print sys.exc_info(), traceback.format_exc()
        return super(CreateView, self).form_valid(form)

class SubmitView(generic.DetailView):

    model = Contact

    template_name = 'contact/submit.html'

    # def email(request):
    #     if request.method == 'GET':
    #         form = ContactForm()
    #     else:
    #         print 'did I get here?'
    #         form = ContactForm(request.POST)
    #         if form.is_valid():
    #             subject_text = form.cleaned_data['subject_text']
    #             email_text = form.cleaned_data['email_text']
    #             message_text = form.cleaned_data['message_text']
    #             try:
    #                 send_mail(subject_text, message_text, email_text,
    #                     ['vaultkeystudios@gmail.com'], fail_silenty=False)
    #             except BadHeaderError:
    #                 return HttpResponse('Invalid header found.')
    #             except:
    #                 print sys.exc_info(), traceback.format_exc()
    #
    #             return redirect('thanks')
    #     return render(request, "contact/detail.html", {'form': form})
