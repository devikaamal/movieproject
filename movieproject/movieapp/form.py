from django import forms
from movieapp.models import Movietb


class movieform(forms.ModelForm):
    class Meta:
        model = Movietb
        fields = "__all__"
