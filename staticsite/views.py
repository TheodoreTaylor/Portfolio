from django.shortcuts import render


# Create your views here.
def index(request):
    return render(
        request, "staticsite/index.html",
    )


def about(request):
    return render(
        request, "staticsite/about.html",
    )


def projects(request):
    return render(
        request, "staticsite/projects.html",
    )


def contact(request):
    return render(
        request, "staticsite/contact.html",
    )
