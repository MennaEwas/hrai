from django.urls import path
from jobvac import views

urlpatterns = [
    path('jobvac/', views.job_list),
    path('jobvac/<int:Announcement_id>/', views.job_detail),
]