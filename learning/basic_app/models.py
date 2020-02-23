from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class modelpage(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    pincode=models.IntegerField()

    def __str__(self):
        return self.name

class UserProfileInfo(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	portfolio_site=models.URLField(blank=True)
	profile_pic=models.ImageField(upload_to='profile_pics',blank=True)