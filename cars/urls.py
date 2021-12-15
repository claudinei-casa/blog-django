from django.urls import path
from . import views
from .views import create, update,delete_car

app_name = "cars"
urlpatterns = [
    path("create/", create, name="create"),
    path("update/<int:pk>/", update, name="update"),
    path("delete/<int:pk>/", delete_car, name="delete"),
    path("", views.CarsListView.as_view(), name='list-cars'),
    path("<slug:slug>/", views.CarsDetailView.as_view(), name="CarDetailsView"),
]
