from django.db import models
# from Crypto.Hash import SHA256
# from codecs import encode,decode

# Create your models here.
class URegister(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(unique = True, max_length = 255)
    passwordHash = models.CharField(max_length = 64)
class Zip(models.Model):
    ngoname= models.CharField(max_length = 30)
    zipcode= models.CharField(max_length = 6)
    email = models.EmailField(unique = True, max_length = 255)
    contactNumber = models.CharField(unique = True, max_length = 10)
    password = models.CharField(max_length = 64,)
    address = models.CharField(max_length = 100)
class Upload(models.Model):
    ngoname= models.CharField(max_length = 30)
    ngoemail= models.CharField(max_length = 30)
    uname= models.CharField(max_length = 30)
    umobile= models.CharField(max_length = 10)
    uemail=models.EmailField(max_length = 255)
    uaddress=models.CharField(max_length = 100)
    umessage=models.CharField(max_length = 100)
    ustatus=models.CharField(max_length=30,default="Pending")
