from django.shortcuts import render
from .models import Article
# Create your views here.
def home(request):
    article=Article.objects.all()

    return render(request,'index.html',{'article':article})

def singles(request,id):
    single=Article.objects.get(id=id)

    return render(request,'single.html',{'single':single})

def portfolio(request):
    return render(request,'pindex.html')