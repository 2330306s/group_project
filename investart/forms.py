from django import forms
from investart.models import NewUser, DevProfile, InvProfile, Project, Contact

#Creating a form for adding a project
class ProjectForm(forms.ModelForm):
    #Different fields
    project_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    project_website = forms.URLField(max_length=50)
    overview = forms.CharField(max_length=150, widget=forms.Textarea, required=True)
    fund_requirement = forms.CharField(max_length=150, widget=forms.Textarea, required=True)
    returns = forms.CharField(max_length=150, widget=forms.Textarea, required=True)
    verified = forms.CharField(widget=forms.HiddenInput(), max_length=3, required=False)
    innovation_score = forms.CharField(widget=forms.HiddenInput(), max_length=25, required=False)
    competition_score = forms.CharField(widget=forms.HiddenInput(), max_length=25, required=False)
    #To be used for the URL
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    #Creating an object using the fields
    class Meta:
        model = Project
        fields = ('project_name', 'email', 'project_website', 'overview', 'fund_requirement', 'returns',)

#Creating a contact form
class ContactForm(forms.ModelForm):
    #Different fields
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=50, required=True)
    concern = forms.CharField(max_length=150, widget=forms.Textarea, required=True)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    #Creating an object using the fields
    class Meta:
        model = Contact
        fields = ('name', 'email', 'concern',)

#Creating a developer registration form
class DevForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    #Creating an object using the fields
    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password')

    #Saving the model
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_dev = True
        if commit:
            user.save()
        return user

#Creating an investor registration form
class InvForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    #Creating an object using the fields
    class Meta:
        model = NewUser
        fields = ('email', 'username', 'password')

    #Saving the model
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_inv = True
        if commit:
            user.save()
        return user

#Creating a developer profile
class DevProfileForm(forms.ModelForm):
    #Creating an object using the fields
    class Meta:
        model = DevProfile
        fields = ()

#Creating an investor profile
class InvProfileForm(forms.ModelForm):
    #Creating an object using the fields
    class Meta:
        model = InvProfile
        fields = ()
