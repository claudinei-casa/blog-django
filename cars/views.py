from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .forms import CadastroCarroForm


@require_http_methods(["GET", "POST"])
def CadastroCarros(request):
    forms = CadastroCarroForm()
    context = {
        'form': CadastroCarroForm
    }
    return render(request, "cadastrar.html", context=context)
