from django.urls import path
from . import views
from .views import Create, CarsListView

app_name = "cars"
urlpatterns = [
    path("new-car/", Create, name="new-car"),
    path("", views.CarsListView.as_view(), name='list-cars'),
]
