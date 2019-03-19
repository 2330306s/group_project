from django import forms
from investart.models import NewUser, DevProfile, InvProfile, ModProfile

class DevForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_dev = True
        if commit:
            user.save()
        return user

class InvForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password')

    def save(self):
        user = super().save(commit=False)
        user.is_inv = True
        if commit:
            user.save()
        return user

class ModForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password')

    def save(self):
        user = super().save(commit=False)
        user.is_mod = True
        if commit:
            user.save()
        return user

class DevProfileForm(forms.ModelForm):
    class Meta:
        model = DevProfile
        fields = ()

class InvProfileForm(forms.ModelForm):
    class Meta:
        model = InvProfile
        fields = ()

class ModProfileForm(forms.ModelForm):
    class Meta:
        model = ModProfile
        fields = ()
