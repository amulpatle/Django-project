from django.db import models

# Create your models here.

class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_varified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)
    
    
class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    min_salary = models.BigIntegerField(default=0)
    max_salary = models.BigIntegerField(default=0)
    job_type = models.CharField(max_length=150,default="null")
    jobcategory = models.CharField(max_length=150,default="null")
    country = models.CharField(max_length=150,default="null")
    highestedu = models.CharField(max_length =150,default=0)
    experience = models.CharField(max_length =150,default=0)
    website = models.CharField(max_length =150,default="null")
    shift = models.CharField(max_length =150,default="null")
    jobdescription = models.CharField(max_length =150,default="null")
    profile_pic = models.ImageField(upload_to="app/img/candidate")
    
class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    website = models.CharField(max_length = 150,default = "")
    Description = models.CharField(max_length = 250,default = "")
    
   
    logo_pic = models.ImageField(upload_to="app/img/company/")
    
class JobDetails(models.Model):
    company_id = models.ForeignKey(Company,on_delete=models.CASCADE)
    jobname = models.CharField(max_length= 250)
    companyname = models.CharField(max_length= 250)
    companyaddress = models.CharField(max_length= 250)
    jobdescription = models.CharField(max_length= 250)
    qualification = models.CharField(max_length= 250)
    responsibility = models.CharField(max_length= 250)
    location = models.CharField(max_length= 250)
    companyemail = models.CharField(max_length= 250)
    companycontact = models.CharField(max_length= 250)
    salarypackage = models.CharField(max_length= 250)
    experience = models.CharField(max_length= 250)
    logo = models.ImageField(upload_to="app/img/jobpost",default="")
    