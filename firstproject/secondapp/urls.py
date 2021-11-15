
from django.urls import path
from .views import emailVerification,otpVerify

urlpatterns = [
    path('verifyEmail/',emailVerification,name = 'verifyEmail'),
    path('verifyOtp/',otpVerify,name = 'otpVerify'),
]