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
    
    
def delete(request,id):
    Todo.objects.get(id=id).delete();
    return redirect("home")
    
    
def edit(request,id):
    todo=Todo.objects.get(id=id)
    try:
        if request.method=="GET":
            return render(request,"edit.html",{'todo':todo})
        
        else:
            title=request.POST["title"]
            description=request.POST["description"]
            
            todo.title=title
            todo.description=description
            
            todo.save()
            return redirect("home")
    except:
        return ("Something Error occured")
    
def delete_all(request):
    Todo.objects.all().delete()
    return redirect("home")
        
def mark_complete(request,id):
    todo=Todo.objects.get(id=id)
    todo.completed= not todo.completed
    todo.save()
    return redirect("home")
    

    

    
    
    
    
    
        