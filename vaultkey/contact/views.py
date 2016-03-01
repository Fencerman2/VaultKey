from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Contact
# Create your views here.
class CreateView(generic.CreateView):

    model = Contact
    template_name = 'contact/detail.html'
    fields = ('name_text', 'email_text',  'subject_text', 'message_text')

class SubmitView(generic.DetailView):

    model = Contact

    template_name = 'contact/submit.html'

    def email(request):
        if request.method == 'GET':
            form = ContactForm()
        else:
            form = ContactForm(request.POST)
            if form.is_valid():
                subject_text = form.cleaned_data['subject_text']
                email_text = form.cleaned_data['email_text']
                message_text = form.cleaned_data['message_text']
                try:
                    send_mail(subject_text, message_text, email_text, ['vaultkeystudios@gmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return redirect('thanks')
        return render(request, "contact/detail.html", {'form': form})
