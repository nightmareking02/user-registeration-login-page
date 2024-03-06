from django.urls import path
from userapp import views

urlpatterns =[
    path('',views.home,),
    path('register',views.register,name='register'),
    path('index/',views.index,name='index'),
     path('user_logout/',views.user_logout,name='user_logout'),
     path('user_update/',views.user_update,name='user_update'),
    path('user_login/',views.user_login,name='user_login'),
    path('dashboard/',views.dashboard,name='dashboard'),
]