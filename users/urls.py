from django.urls import path
from . import views

app_name = 'users'  # This is for namespacing your URLs

urlpatterns = [
    path('', views.home_page, name='home'),  # Home page
]
