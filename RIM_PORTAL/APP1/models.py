from django.db import models
from django.conf import settings
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

# Create your models here.
class Issue(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    example_inc = models.TextField()
    resolution = models.TextField()
    show = models.BooleanField(default=False)
    #user=models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)
    sys_creation_date = models.DateTimeField(default=datetime.now, blank=True)



class Data(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Status = models.CharField(max_length=10, blank=False)
    Date = models.DateField(blank=True, null=True)
