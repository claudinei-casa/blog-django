from django.urls import path
from .views import create, update, delete_car, read, cars_detail

app_name = "cars"
urlpatterns = [
    path("create/", create, name="create"),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete_car, name="delete"),
    path("", read, name='list-cars'),
    path("<int:id>/", cars_detail, name="cars-detail"),
]
