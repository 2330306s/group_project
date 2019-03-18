from django.db import models
from django.contrib.auth.models import User

class DevProfile(models.Model):
    dev = models.OneToOneField(User)
    
    def _str_(self):
        return self.dev.username

class InvProfile(models.Model):
    inv = models.OneToOneField(User)
    
    def _str_(self):
        return self.inv.username

class ModProfile(models.Model):
    mod = models.OneToOneField(User)
    
    def _str_(self):
        return self.mod.username
