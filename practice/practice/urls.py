
from django.urls import path,include
#from django.urls.conf import include  

urlpatterns = [
    path('Home_page/',include("Home_page.urls")),
]
