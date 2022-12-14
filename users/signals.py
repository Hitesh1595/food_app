from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django.dispatch import receiver

from users.models import UserProfile

# used to create profile when user is user created
@receiver(post_save,sender = User)
def build_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user = instance)

@receiver(post_save,sender = User)
def save_profile(sender,instance,**kwargs):
    instance.userprofile.save()