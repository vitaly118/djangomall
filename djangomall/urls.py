from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

from django.contrib.auth import views, forms as auth_forms
from django import forms
from django.utils.translation import gettext_lazy as _

class AuthenticationFormExample(auth_forms.AuthenticationForm):
    username = forms.EmailField(
        min_length=6,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    password = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
class NewLoginView(views.LoginView):
    template_name = 'accounts/login.html'

    form_class = AuthenticationFormExample

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),

    path('accounts/login/', NewLoginView.as_view()),

    path('accounts/', include('django.contrib.auth.urls')),

    prefix_default_language=False
)
