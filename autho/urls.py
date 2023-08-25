from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    #path('login/forgot/', views.forgot, name='forgot'),

]
