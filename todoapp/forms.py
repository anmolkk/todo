from django import forms
from .models import ToDo

class todo_Forms(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = "__all__"
        exclude = ["user"]

class user_form(forms.Form):
    username = forms.CharField(max_length=200, empty_value="username")
    email = forms.EmailField(empty_value="Email")
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    cpassword = forms.CharField(max_length=32, widget=forms.PasswordInput)