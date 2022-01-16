# from typing_extensions import Required
from cProfile import label
from django import forms
from django.core.files.base import File
from django.db.models import query
from django.db.models.expressions import Col
from django.db.models.fields import BLANK_CHOICE_DASH
from django.forms import widgets
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from usermodel.models import *
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, Submit, HTML, Field
from django.core.exceptions import ValidationError
import re
from allauth.account.forms import SignupForm


class SignupForm(forms.ModelForm):

    passwordconf = forms.CharField(widget = forms.PasswordInput(), required=True, label='Password Confirmation')

    class Meta:
        model = User
        fields = ('email', 'password','first_name', 'last_name',)
        widgets = {
            'password':forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['email'].help_text = 'Valid Email Required'
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('email'),
        ),
        Row(
            Column('password'),Column('passwordconf')
        ),
        Row(
            Column('first_name'),Column('last_name'),
        ),
        Submit('submit', 'Sign Up'),
        )

    def clean(self):
        cd = self.cleaned_data
        if cd.get('password') != cd.get('passwordconf'):
            self.add_error('passwordconf', "passwords do not match!")
        return cd
        