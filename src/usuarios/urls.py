from django.urls import path
from usuarios.views import *

urlpatterns = [
    path("", index),

]