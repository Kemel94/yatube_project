from django.http import HttpResponse


def index(request):
    return HttpResponse('def index')

def group_posts(request, slug):
    return HttpResponse('def group_posts')
