from django.http import HttpResponse


def home_view(request):
    return HttpResponse('<h1>Thanks for visiting</h1>')