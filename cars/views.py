from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from .models import Cars
from django.views.decorators.http import require_http_methods
from .forms import CreateCar


@require_http_methods(["GET", "POST"])
def create(request):
    if request.method == "POST":
        forms = CreateCar(request.POST)
        if forms.is_valid():
            forms.save()
        else:
            return render(request, "create.html", context={'form': forms})
    return render(request, "create.html", context={'form': CreateCar})


def delete_car(request, pk):
    transaction = Cars.objects.get(pk=pk)
    if transaction:
        transaction.delete()
    return HttpResponseRedirect('/')


class CarsListView(ListView):
    model = Cars
    fields = "__all__"


class CarsDetailView(DetailView):
    model = Cars


def update(request, pk):
    transaction = Cars.objects.get(pk=pk)
    forms = CreateCar(request.POST or None, instance=transaction)
    if forms.is_valid():
        forms.save()
        return render(request, "create.html", context={'form': CreateCar})
    else:
        return render(request, "create.html", context={'form': forms})
