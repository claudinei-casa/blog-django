from django.shortcuts import render
from django.views.decorators.http import require_http_methods


def base_page(request):
    user = request.user
    return render(request, 'base.html', context={'users': user})
