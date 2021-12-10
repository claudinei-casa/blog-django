from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import CreateCar


@require_http_methods(["GET", "POST"])
def Create(request):  # cadastro

    if request.method == "GET":
        forms = CreateCar()
        context = {
            'form': CreateCar
        }
        return render(request, "cadastrar.html", context=context)
    else:
        forms = CreateCar(request.POST)
        if forms.is_valid():
            forms.save()
            return render(request, "cadastrar.html", context={'form': CreateCar})
        else:
            return render(request, "cadastrar.html", context={'form': forms})


def Delete(request, id):  # deletar
    pass


def update(request):  # atualizar
    pass
