from django.shortcuts import render
from  django.http import HttpResponse
from  django.shortcuts import render
from .models import Article

def home(request):
    posts = Article.objects.order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})
    #res = '<h1>Список стихов</h1>'
    #for post in posts:
        #res += f'<div><h3>{post.title}</h3><div>{post.content}</div></div><hr>'
    #return HttpResponse('<h1>Hello world</h1>')

def test(request):
    return HttpResponse('<h2>Test page</h2>')

def about(request):
    return render(request, 'blog/about.html')
    #return render(request, 'polls/index.html', context)

def contact(request):
    return render(request, 'blog/basic.html',{'values': ['Если вы хотите со мной связаться  буду очень'
                                                ' рад если вы напишете мне на мою электронную почту: ',
                                                'turist70@i.ua']
                                              }
                                   )