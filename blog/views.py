from django.shortcuts import render,redirect
from .models import Article
from django.contrib import messages
from .forms import BlogForm
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
    context={
        'form':BlogForm
    }
    
    return render(request,'createblog.html',context)

def addblog(request):
    if request.method=='POST':
        saved=False
        myblogform=BlogForm(request.POST,request.FILES)
        if myblogform.is_valid():
            
            allblog=Article()
            allblog.reporter=myblogform.cleaned_data['reporter']
            allblog.category=myblogform.cleaned_data['category']
            allblog.title=myblogform.cleaned_data['title']
            allblog.headline=myblogform.cleaned_data['headline']
            allblog.image=myblogform.cleaned_data['image']
            allblog.content=myblogform.cleaned_data['content']
            allblog.save()
            saved=True
           
          
        else:
            myblogform=BlogForm()
            messages.add_message(request,messages.SUCCESS,'you blog was not saved')
            cp={'message':messages,
            'form':BlogForm}
            return render(request,'createblog.html',cp)
        return redirect('/')