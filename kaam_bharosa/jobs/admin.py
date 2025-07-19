from django.contrib import admin
from .models import Job, JobApplication

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'salary', 'duration_days', 'posted_by', 'created_at', 'number_of_workers', 'latitude', 'longitude')
    list_filter = ('category', 'location', 'created_at')
    search_fields = ('title', 'description', 'location', 'posted_by__username')
    ordering = ('-created_at',)

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('job__title', 'applicant__username', 'job__posted_by__username')
    ordering = ('-applied_at',)
