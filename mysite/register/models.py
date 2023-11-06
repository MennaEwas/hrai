from django.db import models

# Create user model 
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100, default='default_password_value')
    groups = models.ManyToManyField(Group, through='UserGroup', related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, through='UserPermission', related_name='custom_user_set')


class UserGroup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

class UserPermission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)
    