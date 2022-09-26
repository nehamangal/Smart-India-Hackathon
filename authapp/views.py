from multiprocessing import context
from pyexpat import model
from re import template
from aiohttp import request
from django.shortcuts import redirect, render,HttpResponseRedirect
from numpy import Inf
from .forms import SignupForm,SignupInfoForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login , logout,update_session_auth_hash
from django.contrib import messages
from . models import Info,Information
from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage
# Create your views here.
def base(request):
    return render(request,'base.html')

def main(request):
    return render(request,'main.html')

def profilenew(request):
    return render(request,'profilenew.html')

def dashboard(request):
    # completeInfo = Information.objects.all()[:4]
    
    if request.user.is_authenticated:
        # name = request.user
        # data = Information('username':request.user)
        # username = request.user
        # username.save()
        if request.method == "POST":
            data = Information()
            data.username = request.user
            name = Information.objects.filter(username = data.username)
            data.name = request.POST.get('name')
            # name = data.name
            data.description = request.POST.get('description')
            # description = data.description
            data.field = request.POST.get('field')
            # field = data.field
            data.image = request.POST.get('image')
            data.targetMarket = request.POST.get('targetMarket')
            # targetMarket = data.targetMarket
            
            data.marketSize = request.POST.get('marketSize')
            data.marketSize1 = request.POST.get('marketSize1')
            data.marketSize2 = request.POST.get('marketSize2')
            data.marketSize3 = request.POST.get('marketSize3')
             

            # marketSize = data.marketSize
            data.save()
            
            # status_list = Information.objects.get(request.user)
            args = {'completeInfo':name}
            messages.success(request, "Registration successful." )
            return render(request,'dashboard.html',args)
        # return render(request,'dashboard.html',{'user':request.user})
    return render(request,'dashboard.html')

def networking(request):
    if request.user.is_authenticated:
        showall = Info.objects.all()
        
        if request.method == 'POST' and request.FILES['upload']:
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            
            return render(request, 'networking.html',{'file_url':file_url,'showall':showall})

        args = {'showall':showall}
        
        return render(request,"networking.html",args)
    # if request.method == "POST":
#        form=SignupInfoForm(data=request.POST,files=request.FILES)
#        if form.is_valid():
#         form.save()
#         obj=form.instance
#         return HttpResponseRedirect(request,"networking.html",{"obj":obj})
#     else:
#       form=SignupInfoForm()
#     img=Info.objects.all()
#     return render(request,"signup.html",{"img":img,"form":form})

def sign_up(request):
    # data = Info.objects.all()
    # print(data)
    if request.method == 'POST':
        
    #     data = Info()
    #     data.name = request.POST.get('name')
    #     data.email = request.POST.get('email')
      
        fm = SignupForm(request.POST)
        if fm.is_valid():
            fm.save()
           
            user = fm.save()
            
            
           
        # if len(request.FILES)!=0:
        # data.image = request.FILES['image']
        # data.image = request.POST.get('image')
        # if len(request.FILES)!=0:
        #    data.image = request.FILES['image']
            
            # Info = fm2.save(commit=False)

            # Info.user = user

            # if 'profile_pic' in request.FILES:
            #     Info.profile_pic = request.FILES['profile_pic']
            # Info.save()
            login(request,user)
            
    
        # upload = request.FILES['upload']
        # fss = FileSystemStorage()
        # file = fss.save(upload.name, upload)
        # file_url = fss.url(file)
            
        # data.save()
            
        messages.success(request, "Registration successful." )
        return redirect('/main/')
        # return render(request, 'profile.html', {'file_url': img_obj})
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        fm = SignupForm()    
    return render(request,'signup.html',{'form':fm})

# Login View
def user_login(request):
    if not request.user.is_authenticated:
      if request.method == 'POST':
        fm = AuthenticationForm(request=request,data = request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username = uname , password = upass)
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully!!')
                return HttpResponseRedirect('/main/')

      else:
        fm =AuthenticationForm()
      return render(request,'userlogin.html' , {'form':fm})

    else:
        return HttpResponseRedirect('/profile/')


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.FILES['upload']:
        
        # if request.method == 'POST' and request.FILES['upload']:
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
        
        # if request.user.is_authenticated:
            return render(request, 'profilenew.html',{'file_url':file_url,'name':request.user,'email':request.user.email})
            # messages.success(request,{'file_url':file_url,'name':request.user,'email':request.user.email})
            # return render(request, 'profile.html',{'name':request.user,'email':request.user.email})
        # else:
        #     return render(request, 'profilenew.html',{'file_url':file_url,'name':request.user,'email':request.user.email})
    
        return render(request, 'profile.html',{'name':request.user,'email':request.user.email})
    else:
        return render(request, 'userlogin.html')

   
    # return render(request, 'profile.html',{'name':request.user,'email':request.user.email})
    # if request.user.is_authenticated:
    # data = Info.objects.get(pk=13)
    # newdata = data.name
    # return render(request,'profile.html',{'data':newdata})
    # context = {}
    # name = request.POST.get('name')
    # context['name'] = name
    # if request.user.is_authenticated:
    #     if request.method == "POST":
	# 	    form = SignupInfoForm(request.POST, request.FILES)
		# if form.is_valid():
		# 	form.save()
		# return redirect("main:upload")
        # if form.is_valid():
        #     form.save()
            # Get the current instance object to display in the template
        #     img_obj = form.instance
        #     return render(request, 'profile.html', {'form': form, 'img_obj': img_obj})
        # else:
        #    form = SignupInfoForm()
        # return render(request, 'profile.html', {'form': form,'name':request.user,'email':request.user.email})
    #    return render(request,'profile.html',{'name':request.user,'email':request.user.email})
    # return render(request,'profile.html',context)
    # else:
    #     return HttpResponseRedirect('/login/')


# Logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

# Change password with Old Password
def user_change_pass(request):
    if request.user.is_authenticated:
      if request.method == 'POST':
        fm = PasswordChangeForm(user = request.user , data = request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request,fm.user)
            messages.success(request,'Password Changes Successfully')
            return HttpResponseRedirect('/profile/')
      else:
       fm = PasswordChangeForm(user = request.user)
      return render(request,'changepass.html',{'form':fm})

    else:
        return HttpResponseRedirect('/login/')

def news(request):
    return render(request,'news.html')

def UserProfile(request):
    model = Info.objects.all()
    return render(request , 'profilenew.html',{'model':model})

def getmentor(request):
    return render(request,'cards.html')

def map(request):
    return render(request,'map.html')
def cardsfront(request):
    return render(request,'cardsfront.html')

def newsfront(request):
    return render(request,'newsfront.html')

def joinhub(request):
    return render(request,'jh.html')


def investors(request):
    if request.user.is_authenticated:
        showall = Info.objects.all()
        
        if request.method == 'POST' and request.FILES['upload']:
            upload = request.FILES['upload']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            
            return render(request, 'investers.html',{'file_url':file_url,'showall':showall})

        args = {'showall':showall}
        
        return render(request,"investers.html",args)
def idea(request):
    return render(request,'ideavali.html')
def pich(request):
    return render(request,'pitchDeck.html')
def go(request):
    return render(request,'goTm.html')
def revenue(request):
    return render(request,'revenueM.html')
def prototype(request):
    return render(request,'prototyping.html')
def fundraising(request):
    return render(request,'fundRasing.html')
def mentorp(request):
    return render(request,'mentor.html')
def mentordesc(request):
    return render(request,'mentordesc.html')
def acv(request):
    return render(request,'accv.html')
def ac(request):
    return render(request,'e.html')
    
    