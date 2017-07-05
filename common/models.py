from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


def make_user_image_path(instance, filename):
    file_extension = filename[filename.rfind('.'):]
    path = 'images/user_avatars/user_' + instance.user.id + file_extension
    return path


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=make_user_image_path, blank=True, null=True)
    reputation = models.BigIntegerField(default=0)
    gold_badges = models.IntegerField(default=0)
    silver_badges = models.IntegerField(default=0)
    bronze_badges = models.IntegerField(default=0)
    answers_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'User profile'
        verbose_name_plural = 'User profiles'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()