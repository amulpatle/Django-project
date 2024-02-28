from django.shortcuts import render,redirect
from .models import *
from random import randint
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
        print("company ReGistration")
        


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


def LoginUser(request):
    if request.POST['role'] == 'candidate':
        email = request.POST['email']
        password = request.POST['password']
        
        user = UserMaster.objects.get(email=email)
        
        if user:
            if user.password == password and user.role == "Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id 
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                return redirect('index')
            else:
                message = "Invalid Password"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User doesnot exist"
            return render(request,"app/login.html",{'msg':message})
                