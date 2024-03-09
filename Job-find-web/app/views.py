from django.shortcuts import render,redirect
from .models import *
from random import randint
from django.core.files.uploadedfile import SimpleUploadedFile
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")


def SingupPage(request):
    return render(request,"app/signup.html")


def RegisterUser(request):
    if request.POST['role'] == 'Candidate':
        role = request.POST['role']
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        user = UserMaster.objects.filter(email=email)
        
        if user:
            message = "User already Exist"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = Candidate.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpvarify.html",{'email':email})
    else:
        # print("company ReGistration")
        role = request.POST['role']
        
        fname = request.POST['firstname']
        lname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        
        user = UserMaster.objects.filter(email=email)
        
        if user:
            message  = "User already Exist"
            return render(request,"app/signup.html",{'msg':message})
        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role,otp=otp,email=email,password=password)
                newcand = Company.objects.create(user_id=newuser,firstname=fname,lastname=lname)
                return render(request,"app/otpvarify.html",{'email':email})
        


def OTPPage(request):
    return render(request,"app/optvarify.html")


def Otpverify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])
    
    user = UserMaster.objects.get(email = email)
    
    if user:
        if user.otp == otp:
            message = "Otp verify successfully"
            return render(request,"app/login.html",{'msg':message})
        else:
            message = "Otp is incorrect"
            return render(request,"app/otpverify.html",{'msg':message})
    else:
        return render(request,"app/signup.html")
    
    
def Loginpage(request):
    return render(request,"app/login.html")


# def LoginUser(request):
#     if request.method == 'POST':
#         if request.POST['role']=='Candidate':
#             email = request.POST['email']
#             password = request.POST['password']
            
#             user = UserMaster.objects.get(email=email)
            
#             if user:
#                 if user.password == password and user.role == "Candidate":
#                     can = Candidate.objects.get(user_id=user)
#                     request.session['id'] = user.id 
#                     request.session['role'] = user.role
#                     request.session['firstname'] = can.firstname
#                     request.session['lastname'] = can.lastname
#                     request.session['email'] = user.email
#                     return redirect('index')
#                 else:
#                     message = "Invalid Password"
#                     return render(request,"app/login.html",{'msg':message})
#             else:
#                 message = "User doesnot exist"
#                 return render(request,"app/login.html",{'msg':message})
#         else:
#             email = request.POST['email']
#             password = request.POST['password']
#             user = UserMaster.objects.get(email=email)
#             if user:
#                 if user.password == password and user.role == 'Company':
#                     com = Company.objects.get(user_id = user)
#                     request.session['id'] = user.id
#                     request.session['role'] = user.role
#                     request.session['firstname'] = user.firstname
#                     request.session['lastname'] = user.lastname
#                     request.session['email'] = user.email
#                     return redirect('companyindex')
#                 else:
#                     message = "Invalid Password"
#                     return render(request,"app/login.html",{'msg':message})

def LoginUser(request):
    if request.method == 'POST':
        if request.POST['role'] == 'Candidate':
            email = request.POST['email']
            password = request.POST['password']
            
            user = UserMaster.objects.get(email=email)
            
            if user:
                if user.password == password and user.role == "Candidate":
                    candidate = Candidate.objects.get(user_id=user)
                    request.session['id'] = user.id 
                    request.session['role'] = user.role
                    request.session['firstname'] = candidate.firstname  # Access firstname from Candidate
                    request.session['lastname'] = candidate.lastname  # Access lastname from Candidate
                    request.session['email'] = user.email
                    return redirect('index')
                else:
                    message = "Invalid Password"
                    return render(request, "app/login.html", {'msg': message})
            else:
                message = "User does not exist"
                return render(request, "app/login.html", {'msg': message})
        else:
            email = request.POST['email']
            password = request.POST['password']
            user = UserMaster.objects.get(email=email)
            if user:
                if user.password == password and user.role == 'Company':
                    company = Company.objects.get(user_id=user)
                    request.session['id'] = user.id
                    request.session['role'] = user.role
                    request.session['firstname'] = company.firstname  # Access firstname from Company
                    
                    request.session['lastname'] = company.lastname  # Access lastname from Company
                    request.session['email'] = user.email
                    request.session['password'] = user.password
                    return redirect('companyindex')
                else:
                    message = "Invalid Password"
                    return render(request, "app/login.html", {'msg': message})
            else:
                message = "User does not exist"
                return render(request, "app/login.html", {'msg': message})
    

def ProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    can = Candidate.objects.get(user_id = user)
    return render(request,"app/profile.html",{'user':user,'can':can})


def UpdateProfile(request, pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == 'Candidate':
        can = Candidate.objects.get(user_id=user)
        can.country = request.POST['country']  # Use request.POST instead of request.post
        can.city = request.POST['city']  # Use request.POST instead of request.post
        can.job_type = request.POST['jobCategory']
        can.highestedu = request.POST['educationLevel']
        can.experience = request.POST['experience']
        # can.website = request.POST['website']
        # can.jobdescription = request.POST['description']
        can.min_salary = request.POST['minSalary']
        can.max_salary = request.POST['maxSalary']
        # can.contact = request.POST['contact']
        # can.profile_pic = request.POST['resume']
        can.save()
        url = f'/profile/{pk}'
        return redirect(url)


def ApplyPage(request,pk):
    user = request.session['id']
    if user:
        cand = Candidate.objects.get(user_id = user)
        job = JobDetails.objects.get(id=pk)
        
    return render(request,"app/company/apply.html",{'user':user,'cand':cand,'job':job})

def ApplyJob(request,pk):
    user = request.session['id']
    if user:
        can = Candidate.objects.get(user_id=user)
        job = JobDetails.objects.get(id=pk)
        education = request.POST['education']
        
        min_salary = request.POST['min_salary']
        max_salary = request.POST['max_salary']
        experience = request.POST['experience']
        Porfolio_web = request.POST['website']
        resume = request.FILES['resume']
        
        newapply = ApplyList.objects.create(candidate=can,job=job,education=education,resume=resume,max_salary=max_salary,min_salary=min_salary,experience=experience)
        message = "Apply done successfully"
        return render(request,"app/company/apply.html",{'msg':message})

############## Company Side ##############

def CompanyIndexPage(request):
    return render(request,"app/company/index.html")

def CompanyProfilePage(request,pk):
    user = UserMaster.objects.get(pk=pk)
    comp = Company.objects.get(user_id = user)
    return render(request,"app/company/profile.html",{'user':user,'comp':comp})

def UpdateCompnyProfile(request,pk):
    user = UserMaster.objects.get(pk=pk)
    if user.role == 'Company':
         comp = Company.objects.get(user_id = user)
         comp.firstname = request.POST['firstname']
         comp.lastname = request.POST['lastname']
         comp.email = request.POST['email']
         comp.contact = request.POST['contact']
         comp.city = request.POST['city']
         comp.state = request.POST['state']
         comp.website = request.POST['website']
         comp.Description = request.POST['Description']
         comp.address = request.POST['address']
         if 'image' in  request.FILES:
             image_file = request.FILES['image']
             comp.logo_pic = image_file
         comp.save()
         url = f"/companyprofile/{pk}"
         
         return redirect(url)
         
        #  comp.logo_pic = request.POST['image']
    
        #     if 'image' in request.FILES:
        #         image_file = request.FILES['image']
        #         comp.logo_pic = image_file
                
                
        # comp.save()
        # url = f"/companyprofile/{pk}"
        # return redirect(url)


def JobPostPage(request):
    return render(request,"app/company/jobpost.html")

def JobDetailSubmit(request):
    if 'id' in request.session:
        user_id = request.session['id']
        user = UserMaster.objects.get(id=user_id)
    # user = UserMaster.objects.get(id=user_id)
    if user.role == "Company":
        comp = Company.objects.get(user_id=user)
        jobname = request.POST['jobname']
        companyname = request.POST['companyname']
        companyaddress = request.POST['companyaddress']
        companywebsite = request.POST['companywebsite']
        jobdescription = request.POST['jobdescription']
        qualification = request.POST['qualification']
        responsibility = request.POST['responsibility']
        location = request.POST['location']
        # companyemail = request.POST['companyemail']
        companycontact = request.POST['companycontact']
        salarypackage = request.POST['salarypackage']
        experience = request.POST['experience']
        logo = request.FILES['image']
        
        newjob = JobDetails.objects.create(company_id=comp,jobname=jobname,companyname=companyname,companyaddress=companyaddress,jobdescription=jobdescription,qualification=qualification,responsibility=responsibility,location=location,companycontact=companycontact,salarypackage=salarypackage,experience=experience,logo=logo,companywebsite=companywebsite)
        
        message = "Job Post SuccessFully"
        return render(request,"app/company/jobpost.html",{'msg':message})
    
    
def JobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/company/jobpostlist.html",{'all_job':all_job})


def CandidateJobListPage(request):
    all_job = JobDetails.objects.all()
    return render(request,"app/job-list.html",{'all_job':all_job})

def companylogout(request):
    del request.session['email']
    del request.session['password']
    return redirect('index')