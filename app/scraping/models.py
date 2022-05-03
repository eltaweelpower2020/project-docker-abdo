from django.db import models
from django.contrib.auth.models import User

class FaceBook_Data_Login(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    facebook_email=models.EmailField(null=True)
    facebook_password=models.CharField(max_length=200,null=True)
     

