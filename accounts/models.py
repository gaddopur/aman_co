from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from PIL import Image
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='download.png', upload_to='profile_pics')
    location = models.CharField(max_length=100, default='New Delhi')
    address = models.TextField(default='New Delhi')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# class Account(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=60, unique=True)
#     username = models.CharField(max_length=30,unique = True)
#     date_joined = models.DateTimeField(verbose_name = 'date-joined',auto_now_add=True)
#     last_login =  models.DateTimeField(verbose_name = 'last-login',auto_now_add=True)
