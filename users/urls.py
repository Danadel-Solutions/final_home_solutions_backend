from django.urls import path, include
from dj_rest_auth.registration.views import VerifyEmailView, ConfirmEmailView


urlpatterns = [
    path(
        'registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ),
     path(
        'account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls')),
]
