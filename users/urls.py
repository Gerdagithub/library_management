from django.urls import path
from . import views
from .views import home_page

app_name = 'users'  # This is for namespacing your URLs

urlpatterns = [
    # path('', views.home_page, name='home_page'),  # Home page
    path('', home_page, name='home_page'), 
]
