from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('job_seeker', 'Job Lena Hai'),
        ('job_provider', 'Job Dena Hai'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True)

    def __str__(self):
        return self.user.username
