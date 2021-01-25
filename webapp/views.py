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


def Register(request):
    return render(request, 'register.html')


def Content(request):
    val1 = 'Anonymous Hacker'
    val2 = 'Hacker Anonymous'
    lists = ['val_1', 'val_2', 'val_3', 'val_4']
    content = {
        'key1': val1,
        'key2': val2,
        'lists': lists
    }
    return render(request, 'content.html', context=content)
