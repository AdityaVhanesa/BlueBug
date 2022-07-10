from django import forms

from user.models import Users


class RaiseBugForm(forms.Form):
    user_name = forms.CharField(label="user", max_length=100)
    bug_title = forms.CharField(label="bug_title", max_length=100)
    bug_description = forms.CharField(label="bug_description")

    def clean_user_name(self):
        user_objects = Users.objects.filter(first_name=self.cleaned_data.get("user_name"))
        if not user_objects:
            return False
        else:
            return user_objects[0]
