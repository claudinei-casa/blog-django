from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Cars
from django.views.decorators.http import require_http_methods
from .forms import CreateCar


@require_http_methods(["GET", "POST"])
def Create(request):

    if request.method == "GET":
        forms = CreateCar()
        context = {
            'form': CreateCar
        }
        return render(request, "create.html", context=context)
    else:
        forms = CreateCar(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, "create.html", context={'form': CreateCar})
        else:
            return render(request, "create.html", context={'form': forms})


def Delete(request, id):  # deletar
    pass


def update(request):  # atualizar
    pass


class CarsListView(ListView):
    model = Cars
    fields = "__all__"


class CarsDetailView(DetailView):
    model = Cars
