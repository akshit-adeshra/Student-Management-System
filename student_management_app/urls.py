from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.DemoPage),
    path('', views.LoginPage),
    path('doLogin/', views.doLogin),
    path('get_user_details/', views.GetUserDetails),
    path('logout_user/', views.LogoutUser),
]
