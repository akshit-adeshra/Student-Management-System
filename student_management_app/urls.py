from django.urls import path
from . import views, HodViews

urlpatterns = [
    path('demo/', views.DemoPage, name="demo"),
    path('', views.LoginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.GetUserDetails, name="get_user_details"),
    path('logout_user/', views.LogoutUser, name="logout_user"),
    path('admin_home/', HodViews.admin_home, name="admin_home"),
    path('add_staff/', HodViews.add_staff, name='add_staff'),
    path('add_staff_save/', HodViews.add_staff_save, name='add_staff_save'),
]
