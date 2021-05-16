from django.db import models
from django.db.models.manager import ManagerDescriptor
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class todo(models.Model):
   
    text = models.CharField(max_length=200)
    priority = models.CharField(max_length=20)
    added_date = models.DateTimeField()
    user1 = models.ForeignKey(settings.AUTH_USER_MODEL,default=1,
                              on_delete=models.CASCADE)
