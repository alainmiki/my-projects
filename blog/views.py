from django.shortcuts import render,redirect
from .models import Article
from django.contrib import messages
# Create your views here.
def home(request):
    article=Article.objects.all()

    return render(request,'index.html',{'article':article})

def singles(request,id):
    single=Article.objects.get(id=id)

    return render(request,'single.html',{'single':single})

def portfolio(request):
    return render(request,'pindex.html')

def createblog(request):
    
    return render(request,'createblog.html')

def addblog(request):
    reporter=request.POST.get('reporter')
    category=request.POST.get('category')
    title=request.POST.get('title')
    headline=request.POST.get('headline')
    image=request.POST.get('image')
    content=request.POST.get('content')
    add=Article.objects.create(reporter=reporter,category=category,title=title,headline=headline,image=image,content=content)

    print(reporter)
    messages.add_message(request,messages.SUCCESS,'you just register')

    cp={'message':messages,
        'image':image}

    return render(request,'createblog.html',cp)