from django.shortcuts import render, HttpResponseRedirect
from .models import Cars
from django.views.decorators.http import require_http_methods
from .forms import CreateCar
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        forms = CreateCar(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            return render(request, "create.html", context={'form': forms})
    return render(request, "create.html", context={'form': CreateCar})


@login_required(login_url="/login/")
def delete_car(request, pk):
    transaction = Cars.objects.get(pk=pk)
    if transaction:
        transaction.delete()
    return HttpResponseRedirect('/cars/')


def read(request):
    cars = Cars.objects.all()
    return render(request, "cars_list.html", context={'cars': cars})


@login_required(login_url='/login/')
def cars_detail(request, id):
    car = Cars.objects.get(id=id)
    return render(request, "cars_detail.html", context={'car': car})


@login_required(login_url="/login/")
def update(request, pk):
    transaction = Cars.objects.get(pk=pk)
    forms = CreateCar(request.POST or None, instance=transaction)
    if forms.is_valid():
        forms.save()
        return render(request, "create.html", context={'form': CreateCar})
    else:
        return render(request, "create.html", context={'form': forms})
