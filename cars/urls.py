from django.urls import path
from .views import Create

app_name = "cars"
urlpatterns = [
    path("new-car/", Create, name="new-car"),
]
