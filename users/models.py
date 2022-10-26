from django.db import models

# Create your models here.
''' use to create custom user model inherit from django '''
from django.contrib.auth.models import User

# extend current user model

class UserProfile(models.Model):

# one to one model (one user one profile)
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(default = 'profile.jpg',upload_to = 'profile_pictures')
    location = models.CharField(max_length = 200)

    def __str__(self):
        return self.user.username  
