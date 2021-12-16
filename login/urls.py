from django.urls import path
from .views import login_user, submit_user, logout_user

app_name = 'login'
urlpatterns = [
    path('', login_user, name='login'),
    # submit sem barra no final pois é um post. se fosse get tem que ter
    path("submit", submit_user, name='submit'),
    path("logout/", logout_user, name="logout_user"),
]
