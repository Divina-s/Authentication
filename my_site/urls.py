from django.urls import path
from.import views


urlpatterns=[
    path('register/', views.register, name ='register'),
    path('', views.login_user, name='login'),
    path('home/',views.home, name='home'),
    path('logout',views.logout_user, name='logout'),
    path('test/', views.test, name='test')

]