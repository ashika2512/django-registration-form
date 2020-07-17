from django.shortcuts import render,redirect,HttpResponse
from django.conf import settings
from django.contrib.auth.models import User 
from .models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def register(request):
    if request.method=="POST":

        username=request.POST['username']
        email=request.POST['email']
        phone=request.POST['number']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1 != pass2:

            messages.warning(request,"password do not match ,please try again")
            return redirect('/register')

        try:



            if User.objects.get(username=username):


                messages.warning(request,"UserName Already Taken")
                return redirect('/register')
        except Exception as identifiers:
            
                pass

      
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.warning(request,"register successfull")
        return redirect('/login')

    return render(request,'register.html')

def handlelogin(request):

    if request.method=='POST':
        
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,"login successfull")
            return redirect("/register")
        else:
            messages.error(request,"invalid credentials")
            return redirect("/login")
    return render(request,'login.html')  


def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('num')
        desc=request.POST.get('desc')

        from_email=settings.EMAIL_HOST_USER
        if len(phone)<10:
           messages.error(request,"phone number is inavalid")
           return render(request,'contact.html')

        if len(desc)<5:
            messages.error(request,"provide valid description")
            return render(request,'contact.html')


        

        myusercontact= Contact(name=name,email=email,phone=phone,desc=desc)
        myusercontact.save()
        return HttpResponse("response has been recorded")
        
    return render(request,'contact.html')


def handlelogout(request):
    logout(request)
    messages.info(request,"logout successfull")
    return redirect('/login')  
