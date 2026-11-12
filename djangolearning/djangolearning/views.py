from os import name

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
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


def aboutus(request, value):
    return render(request, "aboutus.html", {"value": value})


def detail(request, value):
    return render(request, "aboutus.html", {"value": value})


def userform(request):
    # data = {}
    try:
        name = request.POST.get("name")
        email = request.POST.get("email")
        data = {"name": name, "email": email}
        print(f"Name: {name}, Email: {email}")
        url = "about-detail/{}/"
        print(f"Redirecting to: {url.format(name)}")
        return redirect(url.format(name))
    except:
        pass

    return render(request, "user_form.html", data)


def calculater(request):
    if request.method == "POST":
        num1 = int(request.POST.get("num1", 0))
        num2 = int(request.POST.get("num2", 0))
        opr = request.POST.get("opr")
        if opr == "add":
            result = num1 + num2
        elif opr == "subtract":
            result = num1 - num2
        elif opr == "multiply":
            result = num1 * num2
        elif opr == "divide":
            result = num1 / num2 if num2 != 0 else 0
        return render(request, "calculater.html", {"result": result})
    return render(request, "calculater.html")
