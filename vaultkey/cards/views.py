from django.shortcuts import Response

# Create your views here.
def index(request):
    return Response("Hello there. You are at the article index.")

def detail(request, article_id):
    return Response("You're looking at article %s." % article_id)
