from knox import views as knox_views
from django.urls import path
from . import views, auth

urlpatterns =[
    #Create TestModel
    path('create-tm/', views.CUDTestModelAPI.as_view(), name="create-testmodel"),
]


#authentication
urlpatterns += [
  #signup
  path('sign-up/', auth.SignUpAPI.as_view(), name="sign_up"),

  #login users
  path('login/', auth.LoginApI.as_view(), name="login"),

  #logout
  path('logout/', knox_views.LogoutView.as_view(), name='logout'),
  
 ]