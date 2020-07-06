from django.urls import path
from . import views
from tasks import views as vs1


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
]