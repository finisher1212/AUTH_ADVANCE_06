from django.urls.resolvers import URLPattern
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.HomeView,name='home'),
    path('signup/',views.SignUpView,name='signup'),
    path('login/',views.LoginView,name='login'),
    path('logout/',views.LogoutView,name='logout'),
    path('changepwd/',views.Changepassview,name='change_password'),


#reset password urls
path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
 
path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
 
path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
 
path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

]