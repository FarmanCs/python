
from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):

    data = {
        'name': 'admin',
        'age': 30,
        'title': 'Homepage',
        'courses': ['Python', 'Django', 'JavaScript', 'HTML', 'CSS'],
        'numbers': [12, 222, 23, 22,234, 52, 65, 76, 87, 98],
        'students': [
            {'name': 'khan', 'age': 20},
            {'name': 'ali', 'age': 22},
            {'name': 'tayyab', 'age': 19},
        ]
    }

    return render(request, 'homepage.html', data)


def aboutus(request):
    return HttpResponse("This is about us page")


def detail(request, id):
    return HttpResponse(f"This is detail page for id: {id}")
