from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from content_app.models import Blog

# Create your views here
def home(request):
    blogs=Blog.objects.all()
    return render(request,"contentApp/home.html", context={'blogs':blogs})

def add(request):
    if request.method=="GET":
        return render(request,"contentApp/add.html")
    else:
        t=request.POST["title"]
        c=request.POST["content"]
        Blog.objects.create(title=t,content=c,authors_id=1)
        return redirect("home")
    
def edit(request,id):
    blogs=Blog.objects.get(id=id)
    if request.method=="GET":
        return render (request, "contentApp/edit.html",{"blogs":blogs})
    else:
        blog.title=request.POST["title"]
        blog.content=request.POST["content"]
        blog.save()
        return redirect("home")