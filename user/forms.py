import re

from django import forms
from django.contrib import messages
from django.core.exceptions import ValidationError


class UserForm(forms.Form):
    first_name = forms.CharField(label="first_name", max_length=100, empty_value="__NA__")
    last_name = forms.CharField(label="last_name", max_length=100, empty_value="__NA__")
    email = forms.CharField(label="email", max_length=100, empty_value="__NA__")
    password = forms.CharField(label="password", max_length=250, empty_value="__NA__")
    confirm_password = forms.CharField(label="confirm_password", max_length=250, empty_value="__NA__")

    def __init__(self, postRequest, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.postRequest = postRequest
        self.emailRegEx = re.compile(r"^\S+@\S+$")

    def clean_first_name(self):
        data = self.cleaned_data.get("first_name")

        if data == "__NA__":
            messages.error(self.postRequest, "Required", extra_tags="first_name_error")
            raise ValidationError("First Name cannot be empty", code="invalid")
        if len(data) < 2:
            messages.error(self.postRequest, "Must be more than 2 characters", extra_tags="first_name_error")
            raise ValidationError("First Name is less than 2 characters", code='invalid')
        return data.lower()

    def clean_last_name(self):
        data = self.cleaned_data.get("last_name")
        if data == "__NA__":
            messages.error(self.postRequest, "Required", extra_tags="last_name_error")
            raise ValidationError("Last Name cannot be empty", code="invalid")
        if len(data) < 2:
            messages.error(self.postRequest, "Must be more than 2 characters", extra_tags="last_name_error")
            raise ValidationError("Last Name is less than 2 characters", code='invalid')
        return data.lower()

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if data == "__NA__":
            messages.error(self.postRequest, "Required", extra_tags="email_error")
            raise ValidationError("Email cannot be empty", code="invalid")
        if not self.emailRegEx.match(data):
            messages.error(self.postRequest, "Not a valid Email address", extra_tags="email_error")
            raise ValidationError("Email is not valid", code='invalid')
        return data.lower()

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if data == "__NA__":
            messages.error(self.postRequest, "Required", extra_tags="password_error")
            raise ValidationError("Password cannot be empty", code="invalid")
        return data

    def clean_confirm_password(self):
        data = self.cleaned_data.get("confirm_password")
        if data == "__NA__":
            messages.error(self.postRequest, "Required", extra_tags="confirm_password_error")
            raise ValidationError("Password cannot be empty", code="invalid")
        return data

    def clean(self):
        super().clean()
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password != confirm_password:
            messages.error(self.postRequest, "Password is not matching !", extra_tags="confirm_password_error")
            raise ValidationError(
                'Passwords are not matching',
                code='invalid',
            )


class LoginForm(forms.Form):
    email = forms.CharField(label="email", max_length=100, empty_value="__NA__")
    password = forms.CharField(label="password", max_length=250, empty_value="__NA__")

    def __init__(self, postRequest, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.postRequest = postRequest
        self.emailRegEx = re.compile(r"^\S+@\S+$")

    def clean_email(self):
        data = self.cleaned_data.get("email")
        if data == "__NA__":
            messages.error(self.postRequest, "Required", extra_tags="login_email_error")
            raise ValidationError("Email cannot be empty", code="invalid")
        if not self.emailRegEx.match(data):
            messages.error(self.postRequest, "Not a valid Email address", extra_tags="login_email_error")
            raise ValidationError("Email is not valid", code='invalid')
        return data.lower()

    def clean_password(self):
        data = self.cleaned_data.get("password")
        if data == "__NA__":
            messages.error(self.postRequest, "Required", extra_tags="login_password_error")
            raise ValidationError("Password cannot be empty", code="invalid")
        return data
