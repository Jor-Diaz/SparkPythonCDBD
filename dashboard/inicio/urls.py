from django.urls import path
from .views import *

urlpatterns = [	
	path("",inicio),
	path("ver",ver)
]