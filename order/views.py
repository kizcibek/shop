from django.http import HttpResponse


def order(request):
    return HttpResponse('Hello! This is order application')
