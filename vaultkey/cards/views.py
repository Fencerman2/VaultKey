from django.shortcuts import HttpResponse
#
# # Create your views here.
def index(request):
    return HttpResponse("Hello there. You are at the article index.")

def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)
