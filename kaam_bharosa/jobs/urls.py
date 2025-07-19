from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.post_job, name='post_job'),
    path('my-jobs/', views.my_jobs, name='my_jobs'),
    path('applications/<int:job_id>/', views.view_applications, name='view_applications'),

    path('available/', views.job_list, name='job_list'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('application/<int:application_id>/contact/', views.contact_applicant, name='contact_applicant'),
    # path('chat/<int:application_id>/', views.chat_view, name='chat'),


]
