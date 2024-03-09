from django.urls import path,include
from . import views
urlpatterns = [
   path("",views.IndexPage,name="index"),
   path("signup/",views.SingupPage,name="signup"),
   path("register/",views.RegisterUser,name="register"),
   path("otppage/",views.OTPPage,name="otppage"),
   path("opt/",views.Otpverify,name="otp"),
   path("loginpage/",views.Loginpage,name="loginpage"),
   path("loginuser/",views.LoginUser,name="login"),
   path("profile/<int:pk>",views.ProfilePage,name="profile"),
   path('updateprofile/<int:pk>', views.UpdateProfile, name='updateprofile'),
   ################ company side ############
   
   path("companyindex/",views.CompanyIndexPage,name = "companyindex"),
   path("companyprofile/<int:pk>",views.CompanyProfilePage,name="companyprofile"),
   path("updatecompanyprofile/<int:pk>",views.UpdateCompnyProfile,name="updatecompanyprofile"),
   path("jobpostpage/",views.JobPostPage,name="jobpostpage"),
   path("jobpost/",views.JobDetailSubmit,name="jobpost"),
   path("jobpostlist/",views.JobListPage, name="joblistpage"),
   path("joblist/",views.CandidateJobListPage,name="joblist"),
   path("companylogout/",views.companylogout,name="companylogout"),
   path("apply/<int:pk>",views.ApplyPage,name="apply"),
   path("applyjob/<int:pk>",views.ApplyJob,name="applyjob"),
   
]
