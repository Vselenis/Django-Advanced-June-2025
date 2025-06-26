from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    # Add future fields here if needed
    pass


def user_photo_path(instance, filename):
    return f'user_{instance.user.id}/photos/{filename}'

class UserProfile(models.Model):
    FACE_SHAPES = (
        (1, 'Oval'),
        (2, 'Round'),
        (3, 'Square'),
    )

    user = models.OneToOneField('CustomUser', on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(upload_to=user_photo_path, null=True, blank=True)
    face_shape = models.IntegerField(choices=FACE_SHAPES, null=True, blank=True)

    def __str__(self):
        return self.user.username