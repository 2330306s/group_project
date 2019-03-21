from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser

#Creating a model for a project
class Project(models.Model):
    #Fields
    project_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    project_website = models.URLField(max_length=50)
    overview = models.CharField(max_length=150)
    fund_requirement = models.CharField(max_length=150)
    returns = models.CharField(max_length=150)
    verified = models.CharField(max_length=3, default="No")
    innovation_score = models.CharField(max_length=25, default="Verification pending")
    competition_score = models.CharField(max_length=25, default="Verification pending")
    #To be used for the URL
    slug = models.SlugField(blank=True, unique=True)

    #Saving the model
    def save(self, *args, **kwargs):
        self.slug = slugify(self.project_name)
        super(Project, self).save(*args, **kwargs)

    #Defining a plural name for the model
    class Meta:
        verbose_name_plural = 'projects'

    #Getting the name for the admin app
    def __str__(self):
        return self.project_name

#Creating a model for the contact form
class Contact(models.Model):
    #Fields
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    concern = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, unique=True)

    #Saving the model
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Contact, self).save(*args, **kwargs)

    #Defining a plural name for the model
    class Meta:
        verbose_name_plural = 'contacts'

    #Getting the name for the admin app
    def __str__(self):
        return self.name

#Creating a new user class using the abstract user class to define different types of users
class NewUser(AbstractUser):
    #Boolean fields to check for the type of user
    is_dev = models.BooleanField(default=False)
    is_inv = models.BooleanField(default=False)

#Creating a developer profile
class DevProfile(models.Model):
    dev = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)

    #Getting username
    def __str__(self):
        return self.dev.username

#Creating an investor profile
class InvProfile(models.Model):
    inv = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)

    #Getting username
    def __str__ (self):
        return self.inv.username
