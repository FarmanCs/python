from django.http import HttpResponse
from django.shortcuts import render
import logging


def homepage(request):

    data = {
        "name": "admin",
        "age": 30,
        "title": "Homepage",
        "courses": ["Python", "Django", "JavaScript", "HTML", "CSS"],
        "numbers": [12, 222, 23, 22, 234, 52, 65, 76, 87, 98],
        "students": [
            {"name": "khan", "age": 20},
            {"name": "ali", "age": 22},
            {"name": "tayyab", "age": 19},
        ],
    }

    return render(request, "homepage.html", data)


def index(request):
    return render(request, "index.html")


def services(request):
    return render(request, "service.html")


def contact(request):
    return render(request, "contact.html")


def aboutus(request):
    return render(request, "aboutus.html")


def detail(request, id):
    return HttpResponse(f"This is detail page for id: {id}")


logger = logging.getLogger(__name__)


def userform(request):

    try:
        name = request.GET.get("name")
        email = request.GET.get("email")
        print(name, email)
        print(3 + 3)
    except:
        pass

    return render(request, "user_form.html")
