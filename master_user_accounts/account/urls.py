from __future__ import unicode_literals

from django.conf.urls import patterns, url

from account.views import SignupView, LoginView, LogoutView, DeleteView
from account.views import ConfirmEmailView
from account.views import ChangePasswordView, PasswordResetView, PasswordResetTokenView
from account.views import SettingsView


urlpatterns = patterns(
    "",
    url(r"^signup/$", SignupView.as_view(), name="account_signup.urls"),
    url(r"^login/$", LoginView.as_view(), name="account_login.urls"),
    url(r"^logout/$", LogoutView.as_view(), name="account_logout.urls"),
    url(r"^confirm_email/(?P<key>\w+)/$", ConfirmEmailView.as_view(), name="account_confirm_email.urls"),
    url(r"^password/$", ChangePasswordView.as_view(), name="account_password.urls"),
    url(r"^password/reset/$", PasswordResetView.as_view(), name="account_password_reset.urls"),
    url(r"^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$", PasswordResetTokenView.as_view(), name="account_password_reset_token.urls"),
    url(r"^settings/$", SettingsView.as_view(), name="account_settings.urls"),
    url(r"^delete/$", DeleteView.as_view(), name="account_delete.urls"),
)
