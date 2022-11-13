from django.shortcuts import render, HttpResponse
# Create your views here.


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_posts(request, slug):
    return HttpResponse('Главная121 страница')
