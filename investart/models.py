from django.db import models
from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    is_dev = models.BooleanField(default=False)
    is_inv = models.BooleanField(default=False)
    is_mod = models.BooleanField(default=False)

class DevProfile(models.Model):
    dev = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)
        
    def _str_(self):
        return self.dev.username

class InvProfile(models.Model):
    inv = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)
    
    def _str_(self):
        return self.inv.username

class ModProfile(models.Model):
    mod = models.OneToOneField(NewUser, on_delete=models.CASCADE, primary_key=True)
    
    def _str_(self):
        return self.mod.username
