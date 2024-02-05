from django.shortcuts import render

from movieapp.models import Movietb

from movieapp.form import movieform


# Create your views here.

def home(request):
    m = Movietb.objects.all()
    return render(request, 'home.html', {'m': m})


def details(request, p):
    m = Movietb.objects.get(id=p)
    return render(request, 'details.html', {'m': m})


def add(request):

    if (request.method == "POST"):
        form = movieform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return home(request)

    form = movieform()
    return render(request, 'add.html', {'form': form})


def update(request, p):
    m = Movietb.objects.get(id=p)
    if (request.method == "POST"):
        form = movieform(request.POST, request.FILES,instance=m)
        if form.is_valid():
            form.save()
            return home(request)

    form = movieform(instance=m)
    return render(request, 'update.html', {'form': form})


def delete(request, p):
    m = Movietb.objects.get(id=p)
    m.delete()
    return home(request)
