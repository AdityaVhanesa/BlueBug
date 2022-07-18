from django import forms


class RaiseBugForm(forms.Form):
    bug_title = forms.CharField(label="bug_title", max_length=100)
    bug_description = forms.CharField(label="bug_description")
    bug_foundIn = forms.CharField(label="bug_foundIn")
    bug_severityLevel = forms.CharField(label="bug_severityLevel")


class NewCommentForm(forms.Form):
    comment = forms.CharField(label="comment")
