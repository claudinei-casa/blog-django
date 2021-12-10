from django.urls import path
from .views import CadastroCarros

app_name = "cars"
urlpatterns = [
    path("cadastro-carro/", CadastroCarros, name="cadastro-carro"),
]
