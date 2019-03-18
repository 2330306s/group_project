from django import forms
from django.contrib.auth.models import User
from investart.models import DevProfile, InvProfile, ModProfile

class DevForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Dev
        fields = ('username', 'password')

class InvForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Inv
        fields = ('username', 'password')

class ModForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Mod
        fields = ('username', 'password')
