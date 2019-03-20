from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import AbstractUser

class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    overview = models.CharField(max_length=150)
    fund_req = models.CharField(max_length=50)
    returns = models.CharField(max_length=50)
    inn_score = models.IntegerField(default=0)
    slug = models.SlugField(blank=True, unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Project, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    concern = models.CharField(max_length=150)
    slug = models.SlugField(blank=True, unique=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Contact, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'contacts'

    def __str__(self):
        return self.name

class NewUser(AbstractUser):
    is_dev = models.BooleanField(default=False)
    is_inv = models.BooleanField(default=False)
    is_mod = models.BooleanField(default=False)

class DevProfile(models.Model):
    dev = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)
        
    def __str__(self):
        return self.dev.username

class InvProfile(models.Model):
    inv = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)
    
    def __str__ (self):
        return self.inv.username

class ModProfile(models.Model):
    mod = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return self.mod.username
