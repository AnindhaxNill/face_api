from django.db import models

# Create your models here.
class AccountsModel(models.Model):
  title = models.CharField(max_length=100, blank=True, default='')
  name = models.CharField(max_length=255)
  created = models.DateTimeField(auto_now_add=True)


class ImageModel(models.Model):
    name=models.CharField(max_length=255,null=False,default="name")
    account_id=models.IntegerField(null=False,default=0)
    image = models.ImageField(upload_to='images/r_img')