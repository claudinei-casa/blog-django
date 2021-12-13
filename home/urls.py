from django import urls
from django.urls import path
from .views import home_page

app_name = 'home_page'
urlpatterns = [
    path('', home_page, name='index'),
]
