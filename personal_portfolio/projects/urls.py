from django.urls import path
from projects import views

urlpatterns = [
   path("", views.project_index, name="project_index"),
   path("<int:pk>/", views.project_detail, name="project_detail"),
   # value passed in the URL is an integer, and its variable name 
   # is pk. That’s the parameter of your project_detail() view function
]