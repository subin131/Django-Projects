from django.shortcuts import render,redirect
from hot_app.models import Register
# Create your views here.
def home(request):
    if request.method=="GET":
        return render(request,"hot_app/home.html")
    else:
        f=request.POST.get("firstname")
        l=request.POST.get("lastname")
        e=request.POST.get("email")
        p=request.POST.get("password")
        Register.objects.create(firstname=f,lastname=l,email=e,password=p)
        return redirect("/display/")
   


def display(request):
    data=Register.objects.all()
    return render(request,"hot_app/display.html",{"datas":data})