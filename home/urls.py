from django.urls import path
from . import views  # Here, we import views from the current directory

urlpatterns = [
    path('', views.home_view, name='home'),  # Here, we define a URL pattern for the home view
]

