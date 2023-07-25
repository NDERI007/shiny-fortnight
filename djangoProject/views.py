from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def blog(request):
    return render(request, "blog.html")


def gallery(request):
    return render(request, "gallery.html")


def testimonial(request):
    return render(request, "testimonial.html")

