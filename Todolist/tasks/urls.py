from django.urls import path
from .views import home,addtask

urlpatterns = [
    path('', home),
    path('addtask',addtask),
]