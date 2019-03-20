from django import forms
from investart.models import NewUser, DevProfile, InvProfile, ModProfile, Project, Contact

class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    overview = forms.CharField(max_length=150)
    fund_req = forms.CharField(max_length=50)
    returns = forms.CharField(max_length=50)
    inn_score = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Project
        fields = ('name', 'overview', 'fund_req', 'returns',)

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    concern = forms.CharField(max_length=150)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Project
        fields = ('name', 'email', 'concern',)

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
