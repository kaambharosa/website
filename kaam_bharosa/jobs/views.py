from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, JobApplication
from .forms import JobForm
from django.contrib.auth.decorators import login_required

@login_required
def post_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        print("LAT:", request.POST.get('latitude'))
        print("LONG:", request.POST.get('longitude'))

        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user

            

            job.save()
            return redirect('my_jobs')
    else:
        form = JobForm()
        print("Form is invalid:")
        print(form.errors)

    return render(request, 'jobs/post_job.html', {'form': form})

@login_required
def my_jobs(request):
    jobs = Job.objects.filter(posted_by=request.user)
    return render(request, 'jobs/my_jobs.html', {'jobs': jobs})

from django.views.decorators.http import require_POST

@login_required
def view_applications(request, job_id):
    job = get_object_or_404(Job, id=job_id, posted_by=request.user)
    applications = job.applications.all()

    if request.method == "POST":
        app_id = request.POST.get("application_id")
        action = request.POST.get("action")
        app = get_object_or_404(JobApplication, id=app_id, job=job)

        if action == "accept":
            app.status = "accepted"
        elif action == "reject":
            app.status = "rejected"
        app.save()
        return redirect("view_applications", job_id=job.id)

    return render(request, 'jobs/view_applications.html', {
        'job': job,
        'applications': applications
    })

from django.db.models import Q

@login_required
def job_list(request):
    jobs = Job.objects.exclude(posted_by=request.user)
    user_applications = JobApplication.objects.filter(applicant=request.user).values_list('job_id', flat=True)

    # Filter logic
    query = request.GET.get('q')
    salary = request.GET.get('salary')
    location = request.GET.get('location')
    duration = request.GET.get('duration')

    if query:
        jobs = jobs.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if salary:
        jobs = jobs.filter(salary__lte=salary)
    if location:
        jobs = jobs.filter(location__icontains=location)
    if duration:
        jobs = jobs.filter(duration_days__lte=duration)

    return render(request, 'jobs/job_list.html', {'jobs': jobs,
                                                  'user_applications': user_applications})


@login_required
def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    
    # prevent duplicate apply
    existing = JobApplication.objects.filter(job=job, applicant=request.user)
    if not existing.exists():
        JobApplication.objects.create(job=job, applicant=request.user)
    return redirect('job_list')

@login_required
def my_applications(request):
    applications = JobApplication.objects.filter(applicant=request.user).select_related('job')
    return render(request, 'jobs/my_applications.html', {'applications': applications})

@login_required
def contact_applicant(request, application_id):
    application = get_object_or_404(JobApplication, id=application_id)

    # Ensure only job poster or applicant can view
    if request.user != application.applicant and request.user != application.job.posted_by:
        return redirect('job_list')  # unauthorized

    return render(request, 'jobs/contact_each_other.html', {
        'job': application.job,
        'applicant': application.applicant,
        'provider': application.job.posted_by
    })

# @login_required
# def chat_view(request, application_id):
#     application = get_object_or_404(JobApplication, id=application_id)

#     # Optional: restrict access to only job seeker or job provider
#     if request.user != application.applicant and request.user != application.job.posted_by:
#         return redirect('job_list')

#     return render(request, 'jobs/chat.html', {
#         'application': application
#     })

