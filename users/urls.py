from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView
from dj_rest_auth.views import PasswordChangeView
from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    path(
        "registration/account-confirm-email/<str:key>/",
        ConfirmEmailView.as_view(),
    ),
    path(
        "account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path(
        "account-change-password/",
        PasswordChangeView.as_view(),
        name="password_reset_confirm",
    ),
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("token/blacklist/", TokenBlacklistView.as_view(), name="token_blacklist"),
]
