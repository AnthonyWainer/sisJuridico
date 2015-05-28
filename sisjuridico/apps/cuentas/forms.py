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
    recordarme = forms.BooleanField(required=False, initial=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields["username"].widget.input_type = "email"  # ugly hack

        self.helper.layout = Layout(
            Field('username', placeholder="Ingrese Email", autofocus=""),
            Field('password', placeholder="Ingrese Contraseña"),
            #HTML('<a href="{}">¿Has olvidado tu contraseña?</a>'.format(
                #reverse("cuentas:password-reset"))),
            Field('recordarme'),
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


