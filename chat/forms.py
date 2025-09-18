from django import forms

class NicknameForm(forms.Form):
    username = forms.CharField(max_length=50)

class MessageForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={"rows": 2, "cols": 40}))
