from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    latest_article = Article.objects.order_by('-pub_date')[:5]
    output = ', '.join([p.article_text for p in latest_article_list])
    return HttpResponse(output)

def detail(request, article_id):
    return HttpResponse("You're looking at article %s." % article_id)
