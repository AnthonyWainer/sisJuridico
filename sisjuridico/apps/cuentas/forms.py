from __future__ import unicode_literals
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.core.urlresolvers import reverse


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('username', placeholder="Ingrese Email", autofocus=""),
            Field('password', placeholder="Ingrese Contraseña"),
            HTML('<a href="{}">¿Has olvidado tu contraseña?</a>'.format(
                reverse("cuentas:password-reset"))),
            Field('remember_me'),
            Submit('sign_in', 'iniciar sesión',
                   css_class="btn btn-lg btn-primary btn-block"),
            )


class SignupForm(authtoolsforms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["email"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('email', placeholder="Ingrese Email", autofocus=""),
            Field('name', placeholder="Ingrese Nombre Completo"),
            Field('password1', placeholder="Ingrese Contraseña"),
            Field('password2', placeholder="Re-Ingrese Contraseña"),
            Submit('sign_up', 'Registrarse', css_class="btn-warning"),
            )


class PasswordChangeForm(authforms.PasswordChangeForm):

    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('old_password', placeholder="Ingrese Contraseña Antigua",
                  autofocus=""),
            Field('new_password1', placeholder="Ingrese Nueva Contraseña"),
            Field('new_password2', placeholder="Ingrese Nueva Contraseña (de nuevo)"),
            Submit('pass_change', 'Cambiar Contraseña', css_class="btn-warning"),
            )


class PasswordResetForm(authtoolsforms.FriendlyPasswordResetForm):

    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('email', placeholder="Ingrese email",
                  autofocus=""),
            Submit('pass_reset', 'Restablecer Contraseña', css_class="btn-warning"),
            )


class SetPasswordForm(authforms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()

        self.helper.layout = Layout(
            Field('new_password1', placeholder="Ingrese Nueva Contraseña",
                  autofocus=""),
            Field('new_password2', placeholder="Ingrese Nueva Contraseña (de nuevo)"),
            Submit('pass_change', 'Cambiar Contraseña', css_class="btn-warning"),
            )
