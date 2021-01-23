from django.shortcuts import render

from django.http import HttpResponse, JsonResponse


# Create your views here.

def Index(request):
    return HttpResponse('Index')


def Add(request, id, name):
    json_user = {
        'id': id,
        'name': name
    }
    return JsonResponse(json_user)


def Page(request):
    return render(request, 'index.html')
