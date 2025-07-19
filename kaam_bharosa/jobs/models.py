from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    CATEGORY_CHOICES = [
        ('plumber', 'Plumber'),
        ('electrician', 'Electrician'),
        ('mistri', 'Mistri'),
        ('labour', 'Labour'),
        ('halwai', 'Halwai'),
        ('saloon', 'Saloon Worker'),
        ('mechanic', 'Mechanic'),
        ('driver', 'Driver'),
        ('welder', 'Welder'),
        ('painter', 'Painter'),
        ('carpenter', 'Carpenter'),
        ('helper', 'Helper'),
        ('security', 'Security Guard'),
        ('gardener', 'Gardener'),
        ('cleaner', 'Cleaner'),
        ('cook', 'Cook'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    
    # Address format: State > District > Village > Nearest Town
    location = models.CharField(max_length=200)
    
    salary = models.IntegerField()
    duration_days = models.IntegerField()
    number_of_workers = models.IntegerField(default=1)
    
   
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted_jobs')
    created_at = models.DateTimeField(auto_now_add=True)

    latitude = models.CharField(max_length=100, default="0.0")
    longitude = models.CharField(max_length=100,default="0.0")

    def __str__(self):
        return f"{self.title} ({self.category}) - {self.location}"


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='applied')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.applicant.username} -> {self.job.title} ({self.status})"
