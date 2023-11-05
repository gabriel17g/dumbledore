from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NewsForm
from .models import News


def homepage(request):
    return render(request, 'News/index.html')


def all_news(request):
    News_list = News.objects.all()
    context = {'News_list': News_list}
    return render(request, 'News/news_page.html', context)

def single_news(request, news_id):
    current_news = News.objects.get(id=news_id)
    context = {'News': current_news}
    return render(request, 'News/single_news.html', context)


def createnewspage(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('News')
        else:
            return HttpResponse("Couldn't create news page")
    else:
        form = NewsForm()
        content = {"form": form}
        return render(request, "News/create.html", content) 
    

def contactpage(request):
    return render(request, "News/contact.html")

# Create your views here.
