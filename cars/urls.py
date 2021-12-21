from django.urls import path
from .views import *

app_name = "cars"
urlpatterns = [
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete_car, name="delete"),
    path("", read, name='list-cars'),
    path("<int:id>/", cars_detail, name="cars-detail"),
    path("create_brand/", create_brand, name="create_brand"),
    path("create_opt/", create_opt, name="create_opt"),

    # json routes
    path("create/", create, name="create"),
]
