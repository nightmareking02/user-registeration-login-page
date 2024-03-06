from django.shortcuts import render,redirect
from userapp.forms import userForms,user_updatef
from userapp.forms import userprofile
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from userapp.models import userdata
# Create your views here.
def register(request):
    registered = False
    if request.method == 'POST':
        form = userForms(request.POST)
        form1 = userprofile(request.POST,request.FILES)

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
    else:
        form = userForms()
        form1 = userprofile()
    return render (request,'registration.html',{'form':form ,'form1':form1,'registered':registered})


def user_login(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)
        user = authenticate(username=username,password=password)
        print(user)
        if user:
            if user.is_active:
                login(request,user)
                print('Login Success')
                # return HttpResponse('Login Success')
                return redirect('index')
            else:
                return HttpResponse('user is not active')
        else:
            return HttpResponse('Please Check Cred')
    return render (request,'user_login.html',{})
@login_required(login_url='user_login')
def index(request):
    return render(request,'index.html')

@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    return redirect('user_login')

@login_required(login_url='user_login')
def user_update(request):
    user = request.user
    if request.method == 'POST':
        form2 = user_updatef(request.POST, instance=user)
        if form2.is_valid():
            form2.save()
            return redirect('user_login')
        else:
            form2 = user_updatef(instance=user)
    else:
        form2 = user_updatef({'username': user.username, 'email': user.email})
    return render(request,'user_update.html',{'form2':form2})

def home(request):
    return render(request,'home.html')

@login_required(login_url='user_login')
def dashboard(request):
    userdat=userdata.objects.get(user = request.user)
    return render(request,'dashboard.html',{'userdat':userdat})