from django.shortcuts import redirect, render
from blog_app.models import Todo
# Create your views here.
def home(request):
    todos=Todo.objects.all()
    return render(request,"home.html",{'todos':todos})

def add(request):
    if request.method=="GET":
        return render(request,"add.html")
    else:
        t=request.POST["title"]
        d=request.POST["description"]
        Todo.objects.create(title=t,description=d,completed=False)
        return redirect("/home/")
        