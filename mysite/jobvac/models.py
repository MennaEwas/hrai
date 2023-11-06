from django.db import models

'''
Announcement_id
Company_id
Creator
description
is_published
is_remote
max_recommend
position_name
status

{
  "Announcement_id": "2251",
  "Company_id": "YourCompanyID",
  "Creator": "CreatorName",
  "description": "Job Description",
  "is_published": true,
  "is_remote": true,
  "max_recommend": 10,
  "position_name": "Position Name",
  "status": "StatusValue"
}

'''
# Create your models here.
class JobModel(models.Model):
    Announcement_id = models.CharField(max_length=100)
    Company_id = models.CharField(max_length=100)
    Creator = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    is_published = models.BooleanField(default=False)
    is_remote = models.BooleanField(default=False)
    max_recommend = models.IntegerField(default=0)
    position_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['Announcement_id']

