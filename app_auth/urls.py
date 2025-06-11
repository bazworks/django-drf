from django.contrib import admin
from django.urls import path

from .views import (
    ForgotPasswordAPIView,
    LoginView,
    LogoutView,
    OTPRegisterView,
    RegisterView,
    RequestOTPView,
    ResetPasswordAPIView,
    ValidateOTPView,
)

# Auth related URLs
# you should comment out the urls that you don't need below
urlpatterns = [
    # for username/password based login/register
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("forgot-password/", ForgotPasswordAPIView.as_view(), name="forgot-password"),
    path("reset-password/", ResetPasswordAPIView.as_view(), name="reset-password"),
    # for OTP based login/register
    path("request-otp/", RequestOTPView.as_view(), name="request-otp"),
    path("validate-otp/", ValidateOTPView.as_view(), name="validate-otp"),
    path("register-otp/", OTPRegisterView.as_view(), name="register-otp"),
]
