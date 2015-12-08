from django.shortcuts import get_object_or_404, render
from django.shortcuts import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .forms import RequestForm
from .models import Request, Submit
# Create your views here.
class DetailView(generic.DetailView):

    model = Request
    def get_form(request):
        if request.method == 'POST':
            form = RequestForm(request.POST)
            if form.is_valid():
                return render (request, 'requests/submit.html')
        else:
            form = RequestForm()

        return render(request, 'requests/request_detail.html', {'form': form})


class SubmitView(generic.DetailView):

    model = Submit

    template_name = 'requests/submit.html'
