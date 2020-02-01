from django.shortcuts import render, redirect 
from .forms import NewForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import idea 
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import json 
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def homepage(request):
    i = idea.objects.all()
    query = ""
    if request.GET:
        query = request.GET['q']
        i = get_data_queryset(str(query))
    return render(request,"main/home.html", context={"ideas":i})


def register(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = NewForm()
    return render (request, "main/register.html",{"form":form})


def logout_request(request):
    logout(request)
    return redirect("/login")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST )
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request , user)
                return redirect("/home")
            else:
                messages.error (request, "Invalid username or password")
    
    form = AuthenticationForm()
    return render (request, "main/login.html", {"form":form})
    

def delete_idea(request, pk):
    i = idea.objects.get(pk=pk)
    i.delete()
    return redirect('/home')

def edit_idea(request, pk):
    i = idea.objects.get(pk=pk)
    context = {
        'share': i
    }
    return render(request, 'image/edit.html', context)

# def book_objects_pagination(request,PAGENO,SIZE):
    # skip = SIZE * (PAGENO -1)
    # books = Book.objects.all() [skip:(PAGENO * SIZE)]
    # dict = {
    #         "books":list(Book.values("title","name"))
    # }
    # return JsonResponse(dict)

def get_data_queryset(query):
    queryset =[]
    queries = query.split(" ")    
    for q in queries:
        u = User.objects.filter(username__icontains=q)
        ideas = idea.objects.filter(
             Q(ideaPeacher__in=u)).distinct()
        
        for i in ideas:
            queryset.append(i)
    return list(set(queryset))

def show_all_data(request):
    i = idea.objects.all()
    print(type(i))
    dict_type = {"ideas": list(i.values("ideaPeacher","Post_idea","category","date_created"))}
    return JsonResponse(dict_type)

@csrf_exempt
def update_data_json(request, pk):
        i= idea.objects.get(id=pk)
        
        if request.method == "GET":
            return JsonResponse({"Idea":i.Post_idea,"category":i.category})
        else:
            json_body = request.body.decode('utf-8')
            json_data = json.loads(json_body)
            i.Post_idea = json_data['Post_idea']
            i.save()
        return JsonResponse({"message":"Successful!!"})

    
    

    


    