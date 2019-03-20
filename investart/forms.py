from django import forms
from investart.models import NewUser, DevProfile, InvProfile, Project, Contact

class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    project_website = forms.URLField(max_length=50)
    overview = forms.CharField(max_length=150, widget=forms.Textarea, required=True)
    fund_requirement = forms.CharField(max_length=150, widget=forms.Textarea, required=True)
    returns = forms.CharField(max_length=150, widget=forms.Textarea, required=True)
    verified = forms.CharField(widget=forms.HiddenInput(), max_length=3, required=False)
    innovation_score = forms.CharField(widget=forms.HiddenInput(), max_length=25, required=False)
    competition_score = forms.CharField(widget=forms.HiddenInput(), max_length=25, required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Project
        fields = ('project_name', 'email', 'project_website', 'overview', 'fund_requirement', 'returns',)

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    concern = forms.CharField(max_length=150, widget=forms.Textarea, required=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Contact
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

class DevProfileForm(forms.ModelForm):
    class Meta:
        model = DevProfile
        fields = ()

class InvProfileForm(forms.ModelForm):
    class Meta:
        model = InvProfile
        fields = ()
