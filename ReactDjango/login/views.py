from django.shortcuts import render,redirect
from login.models import User
# Create your views here.
def display(request):
    datas=User.objects.all()
    return render(request,"login/display.html",{'data':datas})

def add(request):
    if request.method=="GET":
        return render(request,"login/login.html")
    else:
        uname=request.POST["username"]
        passw=request.POST["password"]
        email=request.POST["email"]
        User.objects.create(username=uname,password=passw,email=email)
        return redirect("display")

def delete(request,id):
    User.objects.get(id=id).delete()
    return redirect("display")

# def edit(request,id):
#     data=User.objects.get(id=id)
#     try:
#         if request.method=="GET":
            