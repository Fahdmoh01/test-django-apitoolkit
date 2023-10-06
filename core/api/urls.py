from knox import views as knox_views
from django.urls import path
from . import views


urlpatterns =[
    #Create TestModel
    path('create-tm/', views.CUDTestModelAPI.as_view(), name="create-testmodel"),
]