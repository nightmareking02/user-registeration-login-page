from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userdata(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=20)
    phone=models.BigIntegerField()
    img=models.ImageField(upload_to='userimg/',blank=True)
    def __str__(self) :
        return self.user.username