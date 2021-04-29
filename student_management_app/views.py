from django.contrib import messages
from django.contrib.auth import login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from student_management_app.EmailBackEnd import EmailBackEnd


def DemoPage(request):
    return render(request, 'demo.html')


def LoginPage(request):
    return render(request, 'login.html')


def doLogin(request):
    if request.method != 'POST':
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return HttpResponseRedirect('/admin_home')
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/")


def GetUserDetails(request):
    if request.user:
        return HttpResponse("User : " + request.user.email + " UserType : " + request.user.user_type)
    else:
        return HttpResponse("Please Login First!")


def LogoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")
