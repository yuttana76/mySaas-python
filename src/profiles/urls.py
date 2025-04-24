

from django.urls import path,include
from . import views
urlpatterns = [
    path("", views.profile_view),
    path("<str:username>/", views.profile_view),
    
]
