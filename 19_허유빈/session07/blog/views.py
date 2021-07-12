from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone

# Create your views here.
def home(request):
    # 블로그의 모든 객체를 가져옴
    blogs = Blog.objects.all()
    # 딕셔너리로 home.html에 보내주기
    return render (request, 'home.html', {'blogs':blogs})

# id : 각 페이지 마다 고유한 id 호출
# >> primary key : 각 데이터를 구분하기 위한 고유한 값
def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog':blog})

def dog(request):
    # 블로그의 모든 객체를 가져옴
    dogs = Dog.objects.all()
    # 딕셔너리로 home.html에 보내주기
    return render (request, 'dog.html', {'dogs':dogs})


def make_post(request):
    if request.method == 'POST':
        new_blog = Blog()
        new_blog.title = request.POST['title']
        new_blog.author = request.POST['author']
        new_blog.image = request.FILES.get('image')
        new_blog.body = request.POST['body']
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('home')
    else : #GET 메소드일 때
        return render(request, 'new.html')


def update(request, id):
    if  request.method == 'POST':
        update_blog = Blog.objects.get(id = id)
        update_blog.title = request.POST['title']
        update_blog.author = request.POST['author']
        update_blog.body = request.POST['body']
        update_blog.save()
        return redirect('detail', update_blog.id)
    else :
        blog = Blog.objects.get(id = id)
        return render(request, 'edit.html', {'blog':blog})


def delete(request, id):
    delete_blog = Blog.objects.get(id = id)
    delete_blog.delete()
    return redirect ('home')

'''Comment '''
def create_comment(request, blog_id):
    if request.method == 'POST':
        comment = Comment()
        comment.blog = get_object_or_404(Blog, pk=blog_id)
        comment.author = request.POST['author']
        comment.content = request.POST['content']
        comment.create_at = timezone.datetime.now()
        comment.save()
        return redirect('detail', blog_id)

def delete_comment(request, blog_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    my_comment.delete()
    return redirect('detail', blog_id)