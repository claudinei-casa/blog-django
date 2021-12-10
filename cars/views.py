from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import NewCar


@require_http_methods(["GET", "POST"])
def Create(request):  # cadastro

    if request.method == "GET":
        forms = NewCar()
        context = {
            'form': NewCar
        }
        return render(request, "cadastrar.html", context=context)
    else:
        forms = NewCar(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, "cadastrar.html", context={'form': NewCar})
        else:
            return render(request, "cadastrar.html", context={'form': forms})


def Delete(request):  # deletar
    pass


def update(request):  # atualizar
    pass
